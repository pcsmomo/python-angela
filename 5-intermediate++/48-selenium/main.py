from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = '/Users/noah/Documents/Study/Study_codes/udemy/python-angela/resources/5-intermediate++/' \
                     '48-selenium-webdriver/chromedriver'
service = Service(chrome_driver_path)
# driver = webdriver.Chrome(executable_path=chrome_driver_path)  # deprecated
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.com")

# driver.close()  # close one tab
driver.quit()  # close whole window
