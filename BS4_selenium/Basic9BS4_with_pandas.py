import pandas as pd
import requests
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
names = soup.find_all("a", class_="title")
# print(names)

product_name = []
for i in names:
    name = i.text
    product_name.append(name)
print(product_name)

prices = soup.find_all("h4",class_="price float-end card-title pull-right")
price_list = []
for i in prices:
    price = i.text
    price_list.append(price)
print(price_list)

Desc = soup.find_all("p",class_="description")
desc_list = []
for i in Desc:
    des = i.text
    desc_list.append(des)
print(desc_list)

Review = soup.find_all("p",class_="review-count")
review_list = []
for i in Review:
    review = i.text
    review_list.append(review)
print(review_list)


df = pd.DataFrame({"Product Name":product_name,"Price":price_list,"Description":desc_list,"Reviews":review_list})
df.to_csv("DatasetUsingPandas.csv")