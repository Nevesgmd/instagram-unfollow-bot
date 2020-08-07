from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/login/")
def login_page():
    return render_template('login.html')


@app.route("/")
def home():
    return redirect(url_for('login_page'))


if __name__ == "__main__":
    app.run()
