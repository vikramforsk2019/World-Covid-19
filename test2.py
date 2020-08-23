import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask
from flask import render_template
import csv
df = pd.read_csv('indiaCovid.csv',sep=',')
#df.dropna(how='any',inplace=True)
print(df.info())
total_deaths=df['Deaths**'].sum()
total_confirm=df['Total Confirmed cases*'].sum()
total_recover=df['Cured/Discharged/Migrated*'].sum()
total_active=df['Active Cases*'].sum()
data = df.to_dict() 
print(len(data['Deaths**']))    
dataset_len=len(data['Deaths**'])
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('main-page.html',data=data,len=dataset_len,tdeath=total_deaths,total_confirm=total_confirm,total_active=total_active,total_recover=total_recover)

@app.route("/charts")
def charts():
	return render_template("charts.html")

if __name__ == '__main__':
    app.run(debug=True, threaded=True)