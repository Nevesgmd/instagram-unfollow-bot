# -- coding: UTF-8 --

# Imports
from backend.selenium_script import InstaBot
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

Window.clearcolor = (0.85, 0.85, 0.9, 0.8)  # Defining background color
Window.size = (800, 460)  # Defining initial window size
Window.minimum_width, Window.minimum_height = (700, 400)  # Defining mininum window size


class PageManager(ScreenManager):
    pass


class LoginPage(Screen):
    pass


with open('app/kivy_interface.kv', encoding='utf-8') as kivy_file:
    kv = Builder.load_string(kivy_file.read())


class InstagramBotInterface(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__insta_bot = InstaBot()
        self.__login_page = kv.get_screen('login')
        Window.bind(on_key_down=self._on_keyboard_down)

    def build(self):
        self.title = 'Instagram Unfollowers'
        return kv

    def _on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40 and kv.current == 'login':  # 40 - Enter key pressed
            self.login()

    def login(self):
        username = self.__login_page.ids.login.text
        password = self.__login_page.ids.password.text
        self.__login_page.ids.login.text = str()
        self.__login_page.ids.password.text = str()
        self.__insta_bot.login(username, password)
        self.print_unfollowers()

    # Provisory, must be changed in next commits
    def print_unfollowers(self):
        unfollowers = self.__insta_bot.get_unfollowers()
        print(unfollowers)
