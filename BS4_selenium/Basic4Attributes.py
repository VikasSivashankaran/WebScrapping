import requests
from bs4 import BeautifulStoneSoup, BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')
#print(soup.div.ul)    all ul tags will be listed
tag = soup.div
print("Tags",tag.attrs)
tag1 = soup.header
atb = (tag1.attrs)

print("Headers tag",tag1.attrs)
print("class:",atb["class"])
