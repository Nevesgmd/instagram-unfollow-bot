from flask import Flask, redirect, url_for, render_template, request
from bot.selenium_script import InstaBot

app = Flask(__name__)


# Defining that when acessing home route it should redirect to the login page route
@app.route("/")
def home():
    return redirect(url_for('login_page'))


# Creating login page route
@app.route("/login/", methods=["POST", "GET"])
def login_page():
    # Getting form info if the request is a POST method
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]
        # Defining global variable inside function so it only opens the Chrome Driver when user click Login button
        global bot
        # Instantiating InstaBot and login to Instagram
        bot = InstaBot()
        bot.login(user, pw)
        # Redirecting to the unfollowers_page
        return redirect(url_for('unfollowers_page'))
    # Rendering template if the request is not a POST method (basically a GET method)
    return render_template('login.html')


# Creating unfollowers page route
@app.route("/unfollowers/")
def unfollowers_page():
    # Getting unfollowers
    unfollowers = bot.get_unfollowers()
    bot.quit()
    # Rendering template with unfollowers list
    return render_template('unfollowers.html', unfollowers=unfollowers)
