from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome back </h1>"

@app.route("/<name>")
def company_page(name):
    return f"<h2>Here is a link to:<h2/> <a href='https://www.{name}.com/'>{name}</a>"

@app.route("/admin/")
def admin():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)


# ======================================================================


from flask import Flask, redirect, url_for, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome back </h1>"

@app.route("/<name>")
def index(name):
    return render_template("index.html", name=name, rnd=random.randint(1, 10))

if __name__ == "__main__":
    app.run(debug=True)


# ======================================================================


from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["nm"]
        return redirect(url_for("user", usr=user_name))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)