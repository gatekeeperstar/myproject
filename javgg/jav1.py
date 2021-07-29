import requests
from bs4 import BeautifulSoup
import sys
import webbrowser

url = "https://javgg.net/jav/waaa-040/"

r = requests.get(url)
# print(r.status_code)


soup = BeautifulSoup(r.text, "lxml")
data = soup.find_all("a")
for d in data:
    if "StreamSB" in d.text:
        print("https:" + d["href"])
        url = "https:" + d["href"]

# url = "https://javgg.net/download/MEFiYkJORSs0Vkw3bUt6TWxvR0VGU1IwZFE4Mkt1bTlyeTVSVmUzdHdPekN0ODlhSVJXVHZNOWJ0eDNhUVlPaw=="
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
url = soup.find("a", {"class": "btn"})["href"]
print("step1:" + url)

r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
data = soup.find_all("a")
id = ""
hashdata = ""
modedata = ""
for d in data:
    # print(d)
    if "onclick" in str(d):
        id = d["onclick"].split("'")[1]
        hashdata = d["onclick"].split("'")[-2]
        if "Normal" in str(d):
            modedata = "n"
        elif "High" in str(d):
            modedata = "h"
        else:
            modedata = "o"
        # print(d["onclick"].split("'")[-2])

url = "https://sbembed1.com/dl?op=download_orig&id={}&mode={}&hash={}".format(
    id, modedata, hashdata
)
# url = "https://sbembed1.com/dl?op=download_orig&id=" + id
print("step2:" + url)
