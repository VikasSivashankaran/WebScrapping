import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")
price = soup.find_all("h4",class_="price float-end card-title pull-right")
print(price)
for i in price:
    print(i.text)

desc = soup.find_all("p",class_ = "description card-text")
for j in desc:
    print(j.text)