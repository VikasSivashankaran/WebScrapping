import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text,"lxml")
print(soup)