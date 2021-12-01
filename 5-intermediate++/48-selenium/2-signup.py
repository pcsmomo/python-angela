import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/noah/Documents/Study/Study_codes/udemy/python-angela/resources/5-intermediate++/' \
                     '48-selenium-webdriver/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Noah")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Kim")

email = driver.find_element(By.NAME, "email")
email.send_keys("dongwoo_333@hanmail.net")
# email.send_keys(Keys.ENTER)

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

time.sleep(3)
driver.quit()  # close whole window
