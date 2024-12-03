import requests
import os

def download_images():
    
    file_name = "hubble.jpeg"
    
    url = input()
    folder_name = input()
    os.makedirs(folder_name, exist_ok=True)

    file_path = os.path.join(folder_name, file_name)
    
    response = requests.get(url)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    download_images()