import re

from PyPDF2 import PdfFileReader


def get_raw_ref_content(pdf_path=None, start_page=37, end_page=53):
    pdf_path = pdf_path or "QI-REV-07-2021-000931_Proof_hi.pdf"
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        refs_raw_text = []
        for i in range(start_page, end_page + 1):
            page = pdf.getPage(i).extractText()
            refs_raw_text += page.replace('\n', '').split(',')
        return refs_raw_text


def avg_word_len(s_: str):
    words_len = list(map(len, s_.split(' ')))
    return sum(words_len) / len(words_len)


def word_count(s_: str):
    s = s_.split(' ')
    return len(s)


def clear_str(s_: str):
    return re.sub(r'[\d+\.\n\t\r\-]', ' ', s_).strip()


def get_refs_from_pdf():
    refs = get_raw_ref_content()
    word_len_threshold = 4.9
    word_count_threshold = 3
    count = 0
    ret = []
    for _ref in refs:
        ref = clear_str(_ref)
        avg_wl = avg_word_len(ref)
        wc = word_count(ref)
        if avg_wl > word_len_threshold and wc > word_count_threshold:
            count += 1
            print('[{:}] {:.4f} {:} {:}'.format(count, avg_wl, wc, _ref))
            ret.append(_ref)
    return ret


if __name__ == '__main__':
    get_refs_from_pdf()
