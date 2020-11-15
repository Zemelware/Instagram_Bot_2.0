from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InstagramBot:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--start-maximized")
        # Disable print statement from Selenium
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(chrome_options=options)

        self.driver.get("https://instagram.com")

        self.wait = WebDriverWait(self.driver, 10)

        self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(
            username, Keys.TAB, password, Keys.ENTER)

        # Wait for page to load
        self.wait.until(EC.invisibility_of_element_located(
            (By.XPATH, "//button/div[text()='Log In']")))

        self.driver.get(f"https://instagram.com/{username}")
