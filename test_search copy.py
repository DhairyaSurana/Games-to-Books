import urllib3
from bs4 import BeautifulSoup
from typing import List
import requests

keyword: str = "best+fantasy+books"
url: str = 'https://www.google.com/search?q=' + keyword
http = urllib3.PoolManager()
r = http.request('GET', url) 
# soup = BeautifulSoup(r.data, "html.parser")
# print(soup.prettify())
# # mains = soup.find_all("div", id = "cnt")
# # for item in mains:
# #     print("\n")
# #     print(item.prettify())
