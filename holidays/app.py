from flask import Flask, render_template, current_app as app, json
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Mannendri's Holidays Project"

@app.route('/holidays')
def holidays():
    #Change the country code below
    country_code = "US" 
    response = requests.get('https://date.nager.at/api/v2/publicholidays/2021/'+country_code)
    data = response.json()

    return render_template('holidays.html',data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
