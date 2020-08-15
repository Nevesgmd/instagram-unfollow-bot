from flask import Flask, redirect, url_for, render_template, request
from bot.selenium_script import InstaBot
from time import sleep

app = Flask(__name__)

bot = InstaBot()


@app.route("/")
def home():
    return redirect(url_for('login_page'))


@app.route("/login/", methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]
        bot.login(user, pw)
        return redirect(url_for('unfollowers_page'))
    return render_template('login.html')


@app.route("/unfollowers/")
def unfollowers_page():
    unfollowers = bot.get_unfollowers()
    return render_template('unfollowers.html', unfollowers=unfollowers)


if __name__ == "__main__":
    app.run()
