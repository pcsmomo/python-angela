from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/noah/Documents/Study/Study_codes/udemy/python-angela/resources/5-intermediate++/' \
                     '48-selenium-webdriver/chromedriver'
service = Service(chrome_driver_path)
# driver = webdriver.Chrome(executable_path=chrome_driver_path)  # deprecated
driver = webdriver.Chrome(service=service)

# Amazon
# driver.get("https://www.amazon.com.au/Razer-Thunderbolt-Dock-Future-Proof-Backward-Compatible/dp/B091BML59Y/ref=sr_1_5?qid=1637822874")
# # price_div = driver.find_element_by_id("corePrice_feature_div")
# price_div = driver.find_element(By.ID, "corePrice_feature_div")
# print(price_div.text)

# Python.org
driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, "q")
print(search_bar.get_attribute("placeholder"))
logo = driver.find_element(By.CLASS_NAME, "python-logo")
print(logo.size)
documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

# Python.org Upcoming Events
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget li time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n],
        "name": event_names[n]
    }

print(events)

# driver.close()  # close one tab
driver.quit()  # close whole window
