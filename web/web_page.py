from flask import Flask, redirect, url_for, render_template, request
from bot.selenium_script import InstaBot

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for('login_page'))


@app.route("/unfollowers/")
def unfollowers_page():
    return render_template('unfollowers.html')


@app.route("/login/", methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]
        bot = InstaBot()
        bot.login(user, pw)
        print(bot.get_unfollowers())
        return redirect(url_for('unfollowers_page'))
    return render_template('login.html')


if __name__ == "__main__":
    app.run()
