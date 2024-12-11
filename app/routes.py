from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/stations")
def stations():
    response = requests.get("https://api.weather.gov/stations")
    if response.status_code == 200:
        return jsonify(response.json())
    return {"error": "Failed to fetch data"}, response.status_code
