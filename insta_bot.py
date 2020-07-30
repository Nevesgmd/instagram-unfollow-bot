from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass


class InstaBot:
    def __init__(self, username, user_pw):
        self.__driver = webdriver.Chrome(ChromeDriverManager().install())
        self.__username = username
        self.__user_password = user_pw
        self.__driver.get("https://instagram.com")
        self.login()

    def login(self):
        WebDriverWait(self.__driver, 20)\
            .until(EC.element_to_be_clickable((By.XPATH, "//input[@name=\"username\"]")))\
            .send_keys(self.__username)
        self.__driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.__user_password)
        WebDriverWait(self.__driver, 20)\
            .until(EC.element_to_be_clickable((By.XPATH,'//button[@type="submit"]')))\
            .click()
        WebDriverWait(self.__driver, 20)\
            .until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))\
            .click()
        WebDriverWait(self.__driver, 20) \
            .until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))) \
            .click()


user_name = str(input('Digite seu nome de usuário, por favor:'))
user_password = getpass('Digite sua senha, por favor:')

insta_bot = InstaBot(user_name, user_password)
