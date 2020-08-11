from flask import Flask, redirect, url_for, render_template, request
from bot.selenium_script import InstaBot

app = Flask(__name__)


@app.route("/")
def home():
    return redirect(url_for('login_page'))


@app.route("/login/", methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]
        bot = InstaBot()
        bot.login(user, pw)
        unfollowers = bot.get_unfollowers()
        return render_template('unfollowers.html', unfollowers=unfollowers)
    return render_template('login.html')


@app.route("/unfollowers/")
def unfollowers_page():
    return render_template('unfollowers.html')


if __name__ == "__main__":
    app.run()
