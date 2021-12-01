from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/noah/Documents/Study/Study_codes/udemy/python-angela/resources/5-intermediate++/' \
                     '48-selenium-webdriver/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

driver.quit()  # close whole window
