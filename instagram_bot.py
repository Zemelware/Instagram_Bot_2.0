from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


class InstagramBot:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        # Disable print statement from Selenium
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(chrome_options=options)

        try:
            self.driver.get("https://instagram.com")

            self.wait = WebDriverWait(self.driver, 10)

            self.wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(
                username, Keys.TAB, password, Keys.ENTER)

            # Wait for page to load
            self.wait.until(EC.invisibility_of_element_located(
                (By.XPATH, "//button/div[text()='Log In']")))
        except:
            self.driver.quit()
            raise Exception("")

        self.driver.get(f"https://instagram.com/{username}")

    def get_not_following_back(self):
        # Check who you're following
        self.driver.find_element_by_xpath(
            "//a[contains(@href, '/following')]").click()

        scroll_box = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[5]/div/div/div[2]")))

        links = self.get_names(scroll_box)
        following = [name.text for name in links if name.text != ""]
        self.driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()

        # Check who's following you
        self.driver.find_element_by_xpath(
            "//a[contains(@href, '/followers')]").click()

        scroll_box = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[5]/div/div/div[2]")))

        links = self.get_names(scroll_box)
        followers = [name.text for name in links if name.text != ""]
        self.driver.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[1]/div/div[2]/button").click()

        self.not_following_back = [
            name for name in following if name not in followers]

        print(self.not_following_back)

    def get_names(self, scroll_box):
        last_ht = 0
        ht = 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);
                                               return arguments[0].scrollHeight;""", scroll_box)
        names = scroll_box.find_elements_by_tag_name("a")
        return names
