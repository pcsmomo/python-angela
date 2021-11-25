import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com.au/Razer-Thunderbolt-Dock-Future-Proof-Backward-Compatible/dp/B091BML59Y/ref=sr_1_5?qid=1637822874"
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
#     "Accept-Language": "en-US,en;q=0.9,ko;q=0.8,zh-CN;q=0.7,zh;q=0.6"
# }

# response = requests.get(url, headers=header)
response = requests.get(url)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(id="corePrice_feature_div").find(name="span", class_="a-offscreen").get_text()
print(price)
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
