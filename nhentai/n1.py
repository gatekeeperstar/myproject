import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import re, time
import os, sys


def get_monthly_url(pattern):
    open("result.txt", "w", encoding="utf-8").close()

    for i in range(1, 10):
        url = "https://nhentai.net/search/?q=COMIC+HOTMILK&page={}".format(i)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "lxml")

        data = soup.find_all("div", {"class": "gallery"})

        for d in data:
            href = "https://nhentai.net" + d.find("a")["href"]
            title = d.find("div", {"class": "caption"}).text
            match = re.search(pattern, title)

            if match is not None:
                print(href, title)
                # print(match.group())
                with open("result.txt", "a", encoding="utf-8") as f:
                    f.write("{} @ {}\n".format(href, title))
        print("page {} is completed".format(i))
        time.sleep(1)


def download_img(target, folder_name, page):
    response = requests.get(target)
    filename = "{}/{}.png".format(folder_name, page)
    if not os.path.isfile(filename):
        file = open(filename, "wb")
        file.write(response.content)
        file.close()
        print(target, " is downloaded!")


def download_comic_book(title, base_url, page_count):
    if not os.path.isdir(title):
        os.mkdir(title)

    # for i in range(1, int(page_count) + 1):
    #     target = "{}/{}.png".format(base_url, i)
    #     print(target)

    # target = "{}/{}.png".format(base_url, 1)
    # download_img(target, title, 1)

    with ThreadPoolExecutor(max_workers=20) as executor:
        for i in range(1, int(page_count) + 1):
            target = "{}/{}.png".format(base_url, i)
            executor.submit(download_img, target, title, i)


# pattern = r"COMIC HOTMILK (\d{4})-(\d{2}) \[Digital\]"
# get_monthly_url(pattern)
tic = time.perf_counter()

title = "COMIC HOTMILK 2021-04 [Digital]"
url = "https://nhentai.net/g/350142/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
page_count = (
    [
        d.text
        for d in soup.find_all("div", {"class": "tag-container field-name"})
        if "page" in d.text.lower()
    ][0]
    .lower()
    .replace("pages:", "")
    .strip()
)
print(page_count)

base_url = soup.find("meta", {"itemprop": "image"})["content"]
# https://t.nhentai.net/galleries/1653211/cover.png
# https://i.nhentai.net/galleries/1653211/1.png
base_url = base_url[: base_url.rfind("/")].replace("t.", "i.")
print(base_url)

download_comic_book(title, base_url, page_count)

toc = time.perf_counter()
print(f"花費時間: {toc - tic:0.4f} 秒")