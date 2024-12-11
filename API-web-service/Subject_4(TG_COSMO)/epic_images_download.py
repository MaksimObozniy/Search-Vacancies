import os
import requests
from utils_function.get_api import get_api_key
from utils_function.create_folder import create_folder



def download_nasaepic_photo():
    
    api_url = "https://api.nasa.gov/EPIC/api/natural/images"
    
    params = {"api_key": NASA_API_KEY}
    
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    epic_data = response.json()
    
    folder_name = "EPIC images"
    create_folder()
    
    for index, photo_data in enumerate(epic_data, start=1):
        
        date = photo_data['date'].split(" ")[0]
        image_name = photo_data['image']
             
        year, month, day = date.split('-')
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png?api_key={NASA_API_KEY}"
        
        file_name = f"epic_{index}.png"
        file_path = os.path.join(folder_name, file_name)
        
        img_response = requests.get(image_url)
        img_response.raise_for_status()
        
        with open(file_path, 'wb') as file:
            file.write(img_response.content)
            
            
if __name__ == "__main__":
    NASA_API_KEY = get_api_key()
    download_nasaepic_photo()
