# import requests
# from bs4 import BeautifulSoup

# r = requests.get('https://www.geeksforgeeks.org/difference-between-descriptive-and-predictive-data-mining/')

#    # check status code for response received
#    # success code - 200
# print(r.content)

#    # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# h2_tags = soup.select('div.text figure.table')
# for h2 in h2_tags:
#    rows = h2.findAll('strong')
#    for row in rows:
#       print(row.text)
#    print(h2.text)

import requests

import re
import csv

url = 'https://webscraper.io/test-sites/e-commerce/allinone'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.flipkart.com/'
}

response = requests.get(url, headers=headers)
print(response.status_code)

# Check if the request was successful
if response.status_code == 200:
    html_content = response.text  # Use text for better handling of the content

    # Regex patterns
    title_pattern = r'title="([^"]+)"'
    discount_rate_pattern = r'<div class="Nx9bqj">₹([\d,]+)</div>'
    original_rate_pattern = r'<div class="yRaY8j">₹([\d,]+)</div>'
    discount_pattern = r'<div class="UkUFwK"><span>([^<]+)</span></div>'
    
    # Find all matches
    titles = re.findall(title_pattern, html_content)
    discount_rates = re.findall(discount_rate_pattern, html_content)
    original_rates = re.findall(original_rate_pattern, html_content)
    discounts = re.findall(discount_pattern, html_content)
    
    # Debug: Print extracted data
    print("Titles:", titles)
    print("Discount Rates:", discount_rates)
    print("Original Rates:", original_rates)
    print("Discounts:", discounts)

    # Ensure that we have the same number of items in each list
    min_length = min(len(titles), len(discount_rates), len(original_rates), len(discounts))
    
    # Write to CSV
    with open('samsung_mobiles.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Discount Rate', 'Original Rate', 'Discount'])
        for i in range(min_length):
            writer.writerow([titles[i], discount_rates[i], original_rates[i] if i < len(original_rates) else 'N/A', discounts[i]])

    print('Data has been written to samsung_mobiles.csv')
else:
    print("Failed to retrieve the page.")





