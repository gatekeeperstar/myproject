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


with open("input.txt", "r", encoding="utf-8") as f:
    urls = f.readlines()
urls = [url for url in urls if "#" not in url and len(url) > 20]

for url in urls:
    if len(url.split("/")) > 6:
        url = "/".join(url.split("/")[:5]) + "/"

    # print(url)
    # input()
    # url = "https://nhentai.net/g/361916/"

    r = requests.get(url)

    with open("result.txt", "w", encoding="utf-8") as f:
        f.write(r.text)

    soup = BeautifulSoup(r.text, "lxml")
    title1 = soup.find("h1", {"class": "title"})
    title2 = soup.find("h2", {"class": "title"})
    title = title2.text if title2 != None else title1.text
    # title = soup.find("h2")
    # 去除不可以出現在目錄的字元
    title = re.sub("""[/:*?"<>|]""", "", title).replace("\\", "")
    print(title)

    if not os.path.isdir("E:/A_COMIC/" + str(title)):
        os.mkdir("E:/A_COMIC/" + str(title))
    export_folder = "E:/A_COMIC/" + str(title) + "/"

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

    ext = (
        [x for x in soup.find_all("img", {"class": "lazyload"})][0]["data-src"]
        .split("/")[-1]
        .split(".")[-1]
    )
    print(ext)

    # i = 1
    # download_image("{}{}.jpg".format(imgurl_base, i), "{}{}.jpg".format(export_folder, i))
    # sys.exit(1)

    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(1, int(pages) + 1):
            executor.submit(
                download_image,
                "{}{}.{}".format(imgurl_base, i, ext),
                "{}{}.{}".format(export_folder, i, ext),
                pages,
            )

# https://i.nhentai.net/galleries/1927914/1.jpg
# https://i.nhentai.net/galleries/1928224/1.png