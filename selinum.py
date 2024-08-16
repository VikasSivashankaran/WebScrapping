from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

element_list = []

# Get user input to select the browser
print("Select the browser to use:")
print("1. Chrome")
print("2. Firefox")
print("3. Edge")
choice = input("Enter the number corresponding to your choice: ")

# Setup the driver based on user choice
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

# Scraping the website
for page in range(1, 3):
    page_url = "https://www.flipkart.com/mobile-phones-store?fm=neo%2Fmerchandising&iid=M_8861da50-a013-4c95-91e0-7c9cdaf54f00_1_372UD5BXDFYS_MC.ZRQ4DKH28K8J&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Mobiles_ZRQ4DKH28K8J&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L0_view-all&cid=ZRQ4DKH28K8J" + str(page)
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME, "wjcEIp")
    price = driver.find_elements(By.CLASS_NAME, "Nx9bqj")
    description = driver.find_elements(By.CLASS_NAME, "Wphh3N")
    rating = driver.find_elements(By.CLASS_NAME, "XQDd")

    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

print(element_list)

driver.close()
