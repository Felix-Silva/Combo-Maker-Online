from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/sf6")
def sf6CharSel():
    return "Street Fighter 6 Character Select (Placeholder)"

@app.route("/tekken8")
def tek8CharSel():
    return "Tekken 8 Character Select (Placeholder)"