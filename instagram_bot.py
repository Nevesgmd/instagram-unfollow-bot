from bot.selenium_script import InstaBot
from getpass import getpass

if __name__ == "__main__":
    username = str(input('Digite seu nome de usuário do Instagram:'))
    password = getpass('Senha:')
    selenium_bot = InstaBot()
    selenium_bot.login(username, password)
    print(selenium_bot.get_unfollowers())
