from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from random import randint
from getpass import getpass


class InstaBot:
    def __init__(self, username, user_pw):
        self.__driver = webdriver.Chrome(ChromeDriverManager().install())
        self.__username = username
        self.__user_password = user_pw
        self.__following = list()
        self.__followers = list()
        self.__driver.get("https://instagram.com")
        self.__driver.set_window_size(1200, 700)
        self.login()

    def login(self):
        WebDriverWait(self.__driver, 20)\
            .until(ec.element_to_be_clickable((By.XPATH, "//input[@name=\"username\"]")))\
            .send_keys(self.__username)
        self.__driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(self.__user_password)
        WebDriverWait(self.__driver, 20)\
            .until(ec.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))\
            .click()
        WebDriverWait(self.__driver, 20)\
            .until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))\
            .click()
        WebDriverWait(self.__driver, 20) \
            .until(ec.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]"))) \
            .click()

    def get_following_followers(self):
        WebDriverWait(self.__driver, 20)\
            .until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/section/'
                                                         'div[3]/div[1]/div/div[2]/div[1]/a')))\
            .click()
        num_following = int(WebDriverWait(self.__driver, 20)
                            .until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]'
                                                                         '/section/main/div/header'
                                                                         '/section/ul/li[3]/a/span'))).text)
        WebDriverWait(self.__driver, 20) \
            .until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/'
                                                         'header/section/ul/li[3]/a/span'))) \
            .click()
        following = self.get_names(num_following)
        num_followers = int(WebDriverWait(self.__driver, 20)
                            .until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]'
                                                                         '/section/main/div/header/'
                                                                         'section/ul/li[2]/a/span'))).text)
        WebDriverWait(self.__driver, 20) \
            .until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/'
                                                         'header/section/ul/li[2]/a/span'))) \
            .click()
        followers = self.get_names(num_followers)

        self.__following = following
        self.__followers = followers

    def get_names(self, num_users):
        scroll_box = WebDriverWait(self.__driver, 20) \
            .until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[2]')))
        for i in range(int(num_users/9)):
            self.__driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
            sleep(randint(500, 1250)/1000)
        print('Finished scrolling.')
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        WebDriverWait(self.__driver, 20) \
            .until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[1]/div/div[2]/button'))) \
            .click()
        return names

    def get_unfollowers(self):
        return [username for username in self.__following if username not in self.__followers]

    def get_not_following_followers(self):
        return [username for username in self.__followers if username not in self.__following]


user_name = str(input('Digite seu nome de usuário, por favor:'))
user_password = getpass('Digite sua senha, por favor:')

insta_bot = InstaBot(user_name, user_password)
insta_bot.get_following_followers()
print(insta_bot.get_unfollowers())
print(insta_bot.get_not_following_followers())
