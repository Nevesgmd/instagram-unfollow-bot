from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
from random import randint


class InstaBot:
    def __init__(self):
        self.__driver = webdriver.Chrome(ChromeDriverManager().install())
        self.__following = list()
        self.__followers = list()

    def login(self, username, pw):
        """Login the user and close initial popups."""
        self.__driver.get("https://instagram.com")
        self.__driver.set_window_size(1200, 700)
        WebDriverWait(self.__driver, 20)\
            .until(ec.element_to_be_clickable((By.XPATH, "//input[@name=\"username\"]")))\
            .send_keys(username)
        self.__driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
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
        """Get the following/followers users and store to private attributes."""
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
        # Calling get_names()
        following = self.get_names(num_following)
        num_followers = int(WebDriverWait(self.__driver, 20)
                            .until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]'
                                                                         '/section/main/div/header/'
                                                                         'section/ul/li[2]/a/span'))).text)
        WebDriverWait(self.__driver, 20) \
            .until(ec.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/'
                                                         'header/section/ul/li[2]/a/span'))) \
            .click()
        # Calling get_names()
        followers = self.get_names(num_followers)

        # Setting following/followers attributes
        self.__following = following
        self.__followers = followers

    def get_names(self, num_users):
        """
        Get usernames in the following/followers panel.
        :param num_users: number of following/followers users
        :return: list of following/followers usernames
        """
        scroll_box = WebDriverWait(self.__driver, 20) \
            .until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[2]')))
        # I decided to iterate num_users/9 times because it works well on most speed connections
        for i in range(int(num_users/9)):
            self.__driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_box)
            sleep(randint(500, 1250)/1000)
        print('Finished scrolling.')
        links = scroll_box.find_elements_by_tag_name('a')
        # Getting names of the elements and storing to a list
        names = [name.text for name in links if name.text != '']
        WebDriverWait(self.__driver, 20) \
            .until(ec.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div[1]/div/div[2]/button'))) \
            .click()
        return names

    def get_unfollowers(self):
        """Return usernames that you're following and doesn't follow back."""
        self.get_following_followers()
        return [username for username in self.__following if username not in self.__followers]
