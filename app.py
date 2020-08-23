from flask import Flask, render_template, request, url_for, session
import json
import requests
from PIL import Image
import matplotlib.pyplot as plt
import pandas as pd
import os
app = Flask(__name__)
df = pd.read_csv('csse_daily.csv',sep=',')
df= df.drop(['FIPS', 'Admin2'], axis=1)
df.dropna(how='any',inplace=True)
print(df.info())
data = df.to_dict()

@app.route("/")
def home_page():
	return render_template('demo.html',name=data)

@app.route("/charts")
def charts():
	return render_template("charts.html")


if __name__ == "__main__":
    app.run(debug = debug)
