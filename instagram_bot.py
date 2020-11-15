from selenium import webdriver
from time import sleep


class InstagramBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://instagram.com")