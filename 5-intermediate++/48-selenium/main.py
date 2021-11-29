from selenium import webdriver

chrome_driver_path = '/Users/noah/Documents/Study/Study_codes/udemy/python-angela/resources/5-intermediate++/48-selenium-webdriver/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com")

# driver.close()  # close one tab
driver.quit()   # close whole window
