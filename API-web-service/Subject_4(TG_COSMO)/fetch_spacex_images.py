import requests
import os
from utils_function.create_folder import create_folder


def fetch_spacex_launch():
    
    folder_name = "Spacex_images"
    create_folder()
    
    default_value = "5eb87d46ffd86e000604b388"
    id_launch = input("Введите id запуска: ") or default_value
    url = f"https://api.spacexdata.com/v5/launches/{id_launch}"
    
    response = requests.get(url)
    response.raise_for_status()
    
    launch_data = response.json()

    images_url = launch_data.get("links", {}).get("flickr", {}).get("original", [])
       
    if not images_url:
        print("Нет изображений для скачивания")
        return
    
    for index, image_url in enumerate(images_url, start=1):
        file_name = f"spacex{index}.jpg"
        file_path = os.path.join(folder_name, file_name)
        
        response = requests.get(image_url)
        response.raise_for_status()
        
        with open(file_path, 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    fetch_spacex_launch()