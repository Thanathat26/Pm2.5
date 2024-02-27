from flask import Flask, render_template
import pandas as pd
import json

app = Flask(__name__)

@app.route('/p')
def index():
    data = pd.read_csv('Clean_data.csv')
    data["DATETIMEDATA"] = pd.to_datetime(data["DATETIMEDATA"])
    data.set_index('DATETIMEDATA', inplace=True)
    data = data.asfreq('H')
    pm25_data = data[['PM25']].to_json(orient='split')

if __name__ == '__main__':
    app.run(debug=True)
