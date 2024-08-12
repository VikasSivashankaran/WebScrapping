from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

element_list = []

options = webdriver.ChromeOptions()
# Use ChromeDriverManager to automatically download and setup the driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

for page in range(1, 3):
    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")

    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

print(element_list)

# Closing the driver
driver.close()
