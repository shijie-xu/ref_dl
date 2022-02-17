# Reference Downloader

## How to download this repo:
- Click the green button **Code** and choose **Download ZIP**.
- Unzip the downloaded file at some place, open your python shell and locate the unzipped directory.

## Usage
1. For first use, please run following command to install required packages.
- `pip install -r requirements.txt`

2. In file `parse_pdf.py`, customize the code as 
```python
def get_raw_ref_content(pdf_path=<You PDF Path>, start_page=<Reference pages start>, end_page=<Reference pages end>):
```

3. Please run following command to download from Sci-Hub.
- `python sci-hub.py` 

## TODO
- [ ] User interface
- [ ] More accurate reference recognition
- [ ] More downloading sources such as Google Scholar
