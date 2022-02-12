import random
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

from parse_pdf import *

download_dir = './'
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    "download.default_directory": download_dir,  # Change default directory for downloads
    "download.prompt_for_download": False,  # To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
})
options.add_argument('--no-sandbox')
browser = webdriver.Chrome('./chromedriver.exe', options=options)
import os
titles = get_refs_from_pdf()
for t in titles:
    if os.path.exists(f'pdfs/{t}.pdf'):
        print('File existed.')
        continue
    print(f'Fetching {t}...')
    browser.delete_all_cookies()

    browser.get('https://sci-hub.mksa.top/')

    searchElem = browser.find_element(By.CSS_SELECTOR, 'input[type="textbox"]')
    searchElem.send_keys(t)

    browser.execute_script("javascript:document.forms[0].submit()")

    # Wait for page to load
    time.sleep(2)

    # Try to press the open button using JS or by fetching the button by its ID

    # This returns error since its unable to fetch open-button id
    # browser.execute_script('javascript:document.querySelector("#open-button").click()')
    try:
        link = browser.find_element(By.ID, "buttons")
        link = link.get_attribute("innerHTML")
        link = link.split('location.href=\'')[1]
        link = link.split("\'")[0]
        if link.startswith('//'):
            link = 'https:' + link
        link = link.replace(r'\/', '/')
        print("Link:", link)
        # r = requests.get(link)
        # open('pdfs/%s.pdf' % t, 'wb').write(r.content)
        browser.get(link)
        
    except:
        pass
    time.sleep(random.randint(5, 10))
