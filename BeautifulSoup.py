import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())

# s = soup.find('div', class_='col-lg-3')
# content = soup.find( class_ = "wrapper" )
#
# print("div ",content)
# # Parsing the HTML
class_list = set()

# Find the 'a' tag
a_tag = soup.find('div')

# Extract the value of the 'href' attribute
href_value = a_tag['class']

# get all tags
tags = {tag.name for tag in soup.find_all()}

# iterate all tags
for tag in tags:

    # find all element of tag
    for i in soup.find_all(tag):

        # if tag has attribute of class
        if i.has_attr("class"):

            if len(i['class']) != 0:
                class_list.add(" ".join(i['class']))

print(class_list)