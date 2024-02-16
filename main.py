import json
import requests
from bs4 import BeautifulSoup
import html

url = 'https://mateserver.onrender.com/'

while True:
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    ul_element = soup.find('ul')
    list_items = ul_element.find_all('li')

    items_list = []

    for li in list_items:
        item_text = li.get_text(strip=True)
        # Extracting the dictionary string and decoding HTML entities
        item_data_str = html.unescape(item_text.split(': {')[1].strip().replace("'", '"').replace("&quot;", '"'))

        try:
            # Parsing the dictionary string to get the required fields
            item_data = json.loads(item_data_str)

            title = item_data['title']
            image = item_data['image']
            para = item_data['para']

            item_info = {
                "title": title,
                "image": image,
                "para": para
            }

            items_list.append(item_info)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    with open('list_items.json', 'w') as json_file:
        json.dump(items_list, json_file, indent=4)

    print("List items saved to list_items.json")
