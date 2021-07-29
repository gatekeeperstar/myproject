import requests  # to get image from the web
import shutil  # to save it locally
from bs4 import BeautifulSoup
import sys, os
from concurrent.futures import ThreadPoolExecutor


def download_image(image_url, filename):
    if not os.path.isfile(filename):
        r = requests.get(image_url, stream=True)
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True

            # Open a local file with wb ( write binary ) permission.
            with open(filename, "wb") as f:
                shutil.copyfileobj(r.raw, f)

            print("Image sucessfully Downloaded: ", filename)
        else:
            print("Image Couldn't be retreived")


url = "https://nhentai.net/g/361916/"
r = requests.get(url)

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(r.text)

soup = BeautifulSoup(r.text, "lxml")
title = soup.find("h2")
print(title.text)

pages = (
    [
        x
        for x in soup.find_all("div", {"class": "tag-container field-name"})
        if "Pages" in x.text
    ][0]
    .find("span", {"class": "name"})
    .text
)
print(pages)

imgurl_base = (
    "https://i.nhentai.net/galleries/"
    + [x for x in soup.find_all("img", {"class": "lazyload"})][0]["data-src"].split(
        "/"
    )[-2]
    + "/"
)
print(imgurl_base)

if not os.path.isdir("output/" + str(title.text)):
    os.mkdir("output/" + str(title.text))
export_folder = "output/" + str(title.text) + "/"

# i = 1
# download_image("{}{}.jpg".format(imgurl_base, i), "{}{}.jpg".format(export_folder, i))
# sys.exit(1)

with ThreadPoolExecutor(max_workers=20) as executor:
    for i in range(1, int(pages) + 1):
        executor.submit(
            download_image,
            "{}{}.jpg".format(imgurl_base, i),
            "{}{}.jpg".format(export_folder, i),
        )

# https://i.nhentai.net/galleries/1927914/1.jpg
