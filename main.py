from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello</h1> <a href='https://www.yahoo.com/'>yahoo.com</a>"

@app.route("/<name>")
def company_page(name):
    return f"<h2>Here is a link to:<h2/> <a href='https://www.{name}.com/'>{name}</a>"


if __name__ == "__main__":
    app.run(debug=True)
