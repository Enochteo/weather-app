import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def index():
    return render_template("weather.html")