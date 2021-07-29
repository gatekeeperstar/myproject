import requests
from bs4 import BeautifulSoup
import sys
import webbrowser

url = "https://javgg.net/jav/300mium-730/"

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
}
r = requests.get(url=url, headers=headers)
print(r.status_code)

with open("result1.txt", "w", encoding="utf-8") as f:
    f.write(r.text)
