from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/sf6")
def sf6CharSel():
    return render_template("sf6CharSel.html")

@app.route("/tekken8")
def tek8CharSel():
    return "Tekken 8 Character Select (Placeholder)"