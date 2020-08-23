import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask
from flask import render_template
import csv
app = Flask(__name__)

@app.route('/')
def root():
    data = []
    with open('indiaCovid.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for entry in reader:
        	data.append(dict(entry))
    print(data[0].keys())
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('main-page.html',data=data, values=values, labels=labels, legend=legend)

@app.route("/charts")
def charts():
	return render_template("charts.html")

if __name__ == '__main__':
    app.run(debug=True, threaded=True)