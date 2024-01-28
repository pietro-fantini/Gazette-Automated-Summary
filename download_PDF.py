from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Specify the correct path to your ChromeDriver
webdriver_path = 'C:/Program Files/Google/chromedriver-win64/chromedriver.exe'

# Initialize the WebDriver using Service
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get('https://www.regione.lazio.it/bur#')

# Locate the PDF link and click it
try:
    pdf_link = driver.find_element(By.CLASS_NAME, 'link_hp_bur_pdf')
    pdf_link.click()
except NoSuchElementException:
    print("Element not found")
    driver.quit()

# Wait for the download to complete
time.sleep(100)

# Don't forget to close the browser
driver.quit()

