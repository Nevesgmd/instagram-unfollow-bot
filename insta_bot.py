from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from getpass import getpass


class InstaBot:
    def __init__(self, username, user_pw):
        self.__driver = webdriver.Chrome(ChromeDriverManager().install())
        self.__username = username
        self.__user_password = user_pw
        self.__driver.get("https://instagram.com")
        sleep(3)
        self.login()

    def login(self):
        self.__driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.__username)
        self.__driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.__user_password)
        self.__driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(5)
        self.__driver.find_element_by_class_name('cmbtv').click()
        sleep(3)
        self.__driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        sleep(5)


user_name = str(input('Digite seu nome de usuário, por favor:'))
user_password = getpass('Digite sua senha, por favor:')

insta_bot = InstaBot(user_name, user_password)
