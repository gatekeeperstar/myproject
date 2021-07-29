from bs4 import BeautifulSoup

data = open("result1.txt", "r", encoding="utf-8").read()
soup = BeautifulSoup(data, "lxml")
data = soup.find_all("a")
id = ""
for d in data:
    # print(d)
    if "quality" in d.text:
        id = d["onclick"].split("'")
        print(id)
        # print(d["onclick"].split("'")[-2])
print(id)