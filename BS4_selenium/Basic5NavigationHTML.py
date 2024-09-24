import requests
from bs4 import BeautifulStoneSoup, BeautifulSoup
from streamlit import header

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
tag = soup.div.p
print(tag.string)

#same method next type

tag = soup.header.div.a.button.span
print(tag.string)