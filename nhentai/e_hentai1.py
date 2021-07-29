import requests  # to get image from the web
import shutil  # to save it locally
from bs4 import BeautifulSoup
import sys, os, re
from concurrent.futures import ThreadPoolExecutor


def download_image(image_url, filename, pages):
    if not os.path.isfile(filename):
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(filename, "wb") as f:
                shutil.copyfileobj(r.raw, f)

            print("{}/{}下載成功".format(filename, pages))
        else:
            print("{}下載失敗".format(filename))


url = "https://e-hentai.org/s/e1331e043c/1407857-3"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
with open("result2.txt", "w", encoding="utf-8") as f:
    f.write(r.text)
base_url = soup.find("div", {"class": "sb"}).find("a")["href"]

r = requests.get(base_url)
with open("result3.txt", "w", encoding="utf-8") as f:
    f.write(r.text)
soup = BeautifulSoup(r.text, "lxml")
title1 = soup.find("h1", {"id": "gn"}).text
title2 = soup.find("h1", {"id": "gj"}).text
print(title1)
print(title2)
print(base_url)
