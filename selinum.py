from selenium import webdriver
import csv
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

print("Select the browser to use:")
print("1. Chrome")
print("2. Firefox")
print("3. Edge")
choice = input("Enter the number corresponding to your choice: ")

if choice == "1":
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
elif choice == "2":
    options = webdriver.FirefoxOptions()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Update this path to your Firefox binary location
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
elif choice == "3":
    options = webdriver.EdgeOptions()
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)
else:
    print("Invalid choice, defaulting to Chrome.")
    options = webdriver.ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

with open('data_mining_comparison.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    for page in range(1, 3):
        url = f"https://www.geeksforgeeks.org/difference-between-descriptive-and-predictive-data-mining/"
        driver.get(url)

        table_divs = driver.find_elements(By.CSS_SELECTOR, 'div.text figure.table')

        for table_div in table_divs:
            rows = table_div.find_elements(By.TAG_NAME, 'tr')

            for row in rows:
                columns = row.find_elements(By.TAG_NAME, 'td')
                if not columns:
                    columns = row.find_elements(By.TAG_NAME, 'th')

                row_data = [col.text.strip() for col in columns]
                writer.writerow(row_data)

    print("CSV file generated successfully.")

driver.quit()
