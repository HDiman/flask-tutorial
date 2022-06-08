from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "radio"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    if "user" in session:
        user_name = session["user"]
    else:
        user_name = "please login"
    return render_template("index.html", user=user_name)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login Successful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged In")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"You have been logged out, {user}!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        flash(f"You are at home, {user}!", "info")
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
