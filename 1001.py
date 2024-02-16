import requests
import json

url = 'https://mateserver.onrender.com/all-data'
response = requests.get(url)

while True:
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()

            # Format the data into a list of dictionaries
            formatted_data = []
            for key, value in data.items():
                item = {
                    "title": value.get("title", ""),
                    "image": value.get("image", ""),
                    "para": value.get("para", "")
                }
                formatted_data.append(item)

            # Write the formatted data to a JSON file
            with open('formatted_data.json', 'w') as file:
                json.dump(formatted_data, file, indent=4)
            print("Data has been successfully written to 'formatted_data.json'.")

        except json.JSONDecodeError:
            print("Error: Failed to decode JSON response from the server.")

    else:
        print(f"Error: Failed to fetch data from the server. Status code: {response.status_code}")
