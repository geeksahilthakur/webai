# # app.py
# from flask import Flask, render_template, jsonify
# import json
# import time
# import requests
# import json

# app = Flask(__name__)

# # Load data from JSON file
# def load_data():
#     with open('formatted_data.json', 'r') as f:
#         data = json.load(f)
#     return data

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/data')
# def get_data():
#     return jsonify(load_data())

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, jsonify
import json
import time
import requests
from threading import Thread

app = Flask(__name__)

# Global variable to store data
global_data = []

# Load data from JSON file
def load_data():
    global global_data
    try:
        with open('formatted_data.json', 'r') as f:
            global_data = json.load(f)
    except FileNotFoundError:
        print("Error: JSON file not found.")
        global_data = []
    except json.JSONDecodeError:
        print("Error: JSON decoding failed.")
        global_data = []

# Fetch data from server and update JSON file
# def update_data():
#     global global_data
#     while True:
#         try:
#             url = 'https://mateserver.onrender.com/all-data'
#             response = requests.get(url)
#             if response.status_code == 200:
#                 try:
#                     # Parse the JSON response
#                     data = response.json()
#                     # Format the data into a list of dictionaries
#                     formatted_data = []
#                     for key, value in data.items():
#                         item = {
#                             "title": value.get("title", ""),
#                             "image": value.get("image", ""),
#                             "para": value.get("para", "")
#                         }
#                         formatted_data.append(item)
#                     # Write the formatted data to a JSON file
#                     with open('formatted_data.json', 'w') as file:
#                         json.dump(formatted_data, file, indent=4)
#                     print("Data has been successfully written to 'formatted_data.json'.")
#                     global_data = formatted_data
#                 except json.JSONDecodeError:
#                     print("Error: Failed to decode JSON response from the server.")
#             else:
#                 print(f"Error: Failed to fetch data from the server. Status code: {response.status_code}")
#             time.sleep(60)  # Fetch data every 60 seconds
#         except requests.RequestException as e:
#             print(f"Error occurred during request: {str(e)}")
#             time.sleep(60)  # Retry after 60 seconds

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    global global_data
    return jsonify(global_data)

if __name__ == '__main__':
    load_data()  # Load data initially
    # update_thread = Thread(target=update_data)
    # update_thread.daemon = True
    # update_thread.start()
    app.run(debug=False, host='0.0.0.0')


