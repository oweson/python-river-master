import requests
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup
url = 'https://list.jd.com/list.html?cat=670%2C671%2C672&go=0'
res = requests.get(url)
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,"html.parser")
print(soup.select('.J_price'))