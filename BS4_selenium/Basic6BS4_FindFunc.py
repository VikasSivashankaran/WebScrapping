#this code will find the first product details

import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text,"lxml")
price = soup.find("h4",{"class":"price float-end card-title pull-right"})
print(price.string)

description = soup.find("p",{"class":"description card-text"})
print(description.string)