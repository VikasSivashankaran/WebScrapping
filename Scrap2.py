import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.geeksforgeeks.org/difference-between-descriptive-and-predictive-data-mining/')

   # check status code for response received
   # success code - 200
print(r.content)

   # Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
h2_tags = soup.select('div.text figure.table')
for h2 in h2_tags:
   rows = h2.findAll('strong')
   for row in rows:
      print(row.text)
   print(h2.text)