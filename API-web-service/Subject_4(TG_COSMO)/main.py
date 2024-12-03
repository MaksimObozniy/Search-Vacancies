import requests
import os


file_name = "hubble.jpeg"
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

folder_name = "images"
os.makedirs(folder_name, exist_ok=True)

file_path = os.path.join(folder_name, file_name)
response = requests.get(url)
response.raise_for_status()

with open(file_path, 'wb') as file:
    file.write(response.content)