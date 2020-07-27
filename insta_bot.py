from selenium import webdriver
from time import sleep
from getpass import getpass


class InstaBot:
    def __init__(self, username, user_pw):
        self.__driver = webdriver.Chrome()
        self.__username = username
        self.__user_password = user_pw
        self.__driver.get("https://instagram.com")
        sleep(2)
        self.login()

    def login(self):
        self.__driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(self.__username)
        self.__driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.__user_password)
        self.__driver.find_element_by_xpath('//button[@type="submit"]').click()
        sleep(2)
        self.__driver.find_element_by_class_name('cmbtv').click()
        sleep(1)
        self.__driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
        sleep(1)


user_name = str(input('Digite seu nome de usuário, por favor:'))
user_password = getpass('Digite sua senha, por favor:')

insta_bot = InstaBot(user_name, user_password)
