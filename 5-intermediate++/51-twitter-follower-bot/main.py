from selenium import webdriver
from selenium.webdriver.chrome.service import Service

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = YOUR CHROME DRIVER PATH
TWITTER_EMAIL = YOUR TWITTER EMAIL
TWITTER_PASSWORD = YOUR TWITTER PASSWORD

service = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=service)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()