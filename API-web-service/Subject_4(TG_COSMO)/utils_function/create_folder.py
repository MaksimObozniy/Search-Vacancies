import os

def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    