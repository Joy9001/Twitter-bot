import os

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

PROMISED_DOWN = 100
PROMISED_UP = 30
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
CLICK_SCRIPT = "arguments[0].click()"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
s = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(options=option, service=s)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = driver
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()

        privacy_accept = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        self.driver.execute_script(CLICK_SCRIPT, privacy_accept)

        go = self.driver.find_element(
            By.XPATH,
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a',
        )
        self.driver.execute_script(CLICK_SCRIPT, go)

        while True:
            down = self.driver.find_element(By.CLASS_NAME, "download-speed")

            down_status = down.get_attribute("data-download-status-value")

            up = self.driver.find_element(By.CLASS_NAME, "upload-speed")

            up_status = up.get_attribute("data-upload-status-value")

            if down_status != "NaN" and up_status != "NaN":
                self.down = down.text
                self.up = up.text
                break

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        self.driver.maximize_window()
        sleep(5)

        try:
            login = self.driver.find_element(By.LINK_TEXT, "Log in")
            self.driver.execute_script(CLICK_SCRIPT, login)

            input_email = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
                    )
                )
            )
            input_email.send_keys(TWITTER_EMAIL)
            input_email.send_keys(Keys.ENTER)
            sleep(5)

            try:
                input_username = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input',
                )
                input_username.send_keys(TWITTER_USERNAME)
                input_username.send_keys(Keys.ENTER)
                print("Found unusual log in and Handled using username.")
                sleep(2)
            except selenium.common.exceptions.NoSuchElementException:
                print("No unusual log in found.")

            input_pass = self.driver.find_element(
                By.XPATH,
                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
            )
            input_pass.send_keys(TWITTER_PASSWORD)
            input_pass.send_keys(Keys.ENTER)
        except selenium.common.exceptions.NoSuchElementException:
            input_email = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input',
                    )
                )
            )
            input_email.send_keys(TWITTER_EMAIL)
            input_email.send_keys(Keys.ENTER)

            sleep(5)

            try:
                input_username = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input',
                )
                input_username.send_keys(TWITTER_USERNAME)
                input_username.send_keys(Keys.ENTER)
                print("Found unusual log in and Handled using username.")
                sleep(2)
            except selenium.common.exceptions.NoSuchElementException:
                print("No unusual log in found.")

            input_pass = WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input',
                    )
                )
            )
            input_pass.send_keys(TWITTER_PASSWORD)
            input_pass.send_keys(Keys.ENTER)

        sleep(10)

        click_post = self.driver.find_element(
            By.XPATH,
            '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div/span',
        )
        self.driver.execute_script(CLICK_SCRIPT, click_post)
        sleep(3)

        write_msg = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div/span/br',
        )
        msg = f"Hey Internet Provider, why is my internet speed {self.down}Mbps down / {self.up}Mbps up when I pay for {PROMISED_DOWN}Mbps down/{PROMISED_UP}Mbps up?"
        write_msg.send_keys(msg)
        sleep(3)

        # outclick = self.driver.find_element(By.XPATH,
        #                                     '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[1]')
        # self.driver.execute_script(CLICK_SCRIPT, outclick)
        self.driver.find_element(By.XPATH, "//body").click()
        sleep(2)

        save = self.driver.find_element(
            By.XPATH,
            '//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span',
        )
        self.driver.execute_script(CLICK_SCRIPT, save)
        print("Tweet saved as draft.")


mybot = InternetSpeedTwitterBot()
mybot.get_internet_speed()
print(mybot.up)
print(mybot.down)
mybot.tweet_at_provider()