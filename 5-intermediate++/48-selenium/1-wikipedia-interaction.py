import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/noah/Documents/Study/Study_codes/udemy/python-angela/resources/5-intermediate++/' \
                     '48-selenium-webdriver/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()
print(article_count.text)

# all_portals = driver.find_element_by_link_text("All portals")
all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(2)
driver.quit()  # close whole window
