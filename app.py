from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    coordinates = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    return render_template("index.html", coordinates=coordinates)