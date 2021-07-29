import requests
import re

# from bs4 import BeautifulSoup

# # https://nhentai.net/g/361947/
# # https://nhentai.net/g/361937/7/

# a = "https://nhentai.net/g/361947/"
# print(len(a.split("/")))

# a = "https://nhentai.net/g/361937/7/"
# print(len(a.split("/")))

# print(a.split("/"))
# if len(a.split("/")) > 6:
#     a = "/".join(a.split("/")[:5]) + "/"
# print(a)

# # url = "https://nhentai.net/g/361866/"
# url = "https://nhentai.net/g/361883/"
# r = requests.get(url)

# soup = BeautifulSoup(r.text, "lxml")
# title1 = soup.find("h1", {"class": "title"})
# title2 = soup.find("h2", {"class": "title"})
# title = title2.text if title2 != None else title1.text
# # print(title)
# # print(title1)
# # print(title2)

# txt = """KKK\/:[黒ねこ赤リボン (神代竜)] メイドライブ!ニジガク支店コンカフェアイドル同好会 (ラブライブ! 虹ヶ咲学園スクールアイドル同好会) [中国翻訳]*?\"<>|def"""
# print(txt)
# txt = re.sub("""[/:*?"<>|]""", "", txt).replace("\\", "")
# print(txt)

url = "https://e-hentai.org/g/1407857/32aad2cdb3/"
url = "https://e-hentai.org/s/e1331e043c/1407857-3"
r = requests.get(url)
print(r.status_code)
with open("result2.html", "w", encoding="utf-8") as f:
    f.write(r.text)
