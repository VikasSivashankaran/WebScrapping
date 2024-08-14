import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
r = requests.get('https://www.geeksforgeeks.org/difference-between-descriptive-and-predictive-data-mining/')

# Check if the request was successful
if r.status_code == 200:
    # Parsing the HTML content
    soup = BeautifulSoup(r.content, 'html.parser')

    # Select the specific div containing the table of interest
    table_divs = soup.select('div.text figure.table')

    # Prepare data for CSV
    data = []

    # Iterate over each table found in the div
    for table_div in table_divs:
        # Find all rows within each table
        rows = table_div.findAll('tr')
        
        for row in rows:
            # Find all columns within each row
            columns = row.findAll('td')
            if not columns:
                # If <td> not found, check for <th> for header rows
                columns = row.findAll('th')

            # Extract text from each column
            row_data = [col.get_text(strip=True) for col in columns]
            
            # Append the row data to the data list
            data.append(row_data)

    # Write data to a CSV file
    with open('data_mining_comparison.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write rows to CSV
        for row in data:
            writer.writerow(row)

    print("CSV file generated successfully.")
else:
    print(f"Failed to retrieve the page. Status code: {r.status_code}")
