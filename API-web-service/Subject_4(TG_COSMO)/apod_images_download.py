from utils_function.get_api import get_api_key
from utils_function.create_folder import create_folder
import requests
import os


def nasa_apod():
    
    url_api = "https://api.nasa.gov/planetary/apod"
    
    params = {
        "api_key": NASA_API_KEY,
        "count": 30
    }
    
    response = requests.get(url_api, params=params)
    response.raise_for_status()
    
    folder_name = "Apod_images"
    create_folder()
    
    data_photo_day = response.json()
    
    for index, photo_data in enumerate(data_photo_day, start=1):
        image_link = photo_data.get("hdurl")
        
        if not image_link:
            continue
        
        file_name = f"apod_{index}.jpg"
        file_path = os.path.join(folder_name, file_name)
        
        img_response = requests.get(image_link)
        img_response.raise_for_status()
            
        with open(file_path, 'wb') as file:
            file.write(img_response.content)
                

if __name__ == "__main__":
    NASA_API_KEY = get_api_key()
    nasa_apod()
    