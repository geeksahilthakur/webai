# app.py
from flask import Flask, render_template, jsonify
import json
import time
import requests
import json

app = Flask(__name__)

# Load data from JSON file
def load_data():
    with open('formatted_data.json', 'r') as f:
        data = json.load(f)
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    return jsonify(load_data())

if __name__ == '__main__':
    app.run(debug=True)
