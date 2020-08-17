from flask import Flask, render_template, request, url_for
import json
import requests
from PIL import Image
import matplotlib.pyplot as plt
app = Flask(__name__)
host = "127.0.0.1"
port = 5000
debug = True

@app.route("/")
def home_page():
	return render_template("main-page.html")

if __name__ == "__main__":
    app.run(debug = debug)
