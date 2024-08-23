import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('https://www.geeksforgeeks.org/difference-between-descriptive-and-predictive-data-mining/')

if r.status_code == 200:
    soup = BeautifulSoup(r.content, 'html.parser')

    table_divs = soup.select('div.text figure.table')

    data = []

    for table_div in table_divs:
        rows = table_div.findAll('tr')
        
        for row in rows:
            columns = row.findAll('td')
            if not columns:
                columns = row.findAll('th')

            row_data = [col.get_text(strip=True) for col in columns]
            
            data.append(row_data)

    with open('data_mining_comparison.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        for row in data:
            writer.writerow(row)

    print("CSV file generated successfully.")
else:
    print(f"Failed to retrieve the page. Status code: {r.status_code}")
