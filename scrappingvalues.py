import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

print(r)
print(r.content)
# check status code for response received
# success code - 200
#print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
h1_tags = soup.select('div.container div.navbar-header')
for h1 in h1_tags:
   print(h1.text)
print(soup)

# r = requests.get('https://toscrape.com/')

#    # check status code for response received
#    # success code - 200
#    # print(r)

#    # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# h1_tags = soup.select('div.container div.row div.col-md-6 table.table')
# for h1 in h1_tags:
#    rows = h1.findAll('tr')
#    for row in rows:
#       print(row.text)
   #print(h1.text)



