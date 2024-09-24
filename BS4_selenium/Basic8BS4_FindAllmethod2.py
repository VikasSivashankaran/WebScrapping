import requests
from bs4 import BeautifulSoup
import re #regular expression

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text,"lxml")

#execute if want

data = soup.find_all(["h4","a","p"])
data1= soup.find_all(string = "Galaxy Tab")
print(data)
print(data1)

data = soup.find_all(string = re.compile("Idea"))
print(data)


