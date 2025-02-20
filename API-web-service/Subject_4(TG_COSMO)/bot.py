import telegram
import os
import random
import time
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN") 
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
PUBLISH_DELAY = int(os.getenv("PUBLISH_DELAY", 5))


bot = telegram.Bot(token=BOT_TOKEN)


def get_photo_list(directory):
    photo_list =[]
    for root, _, files in os.walk(directory):
        for filen in files:
            if filen.lower().endswith((".jpg", ".jpeg", ".png")):
                photo_list.append(os.path.join(root, filen))
    return photo_list  


def publish_photo(photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=photo)
        print(f"Фото опубликовано {photo_path}")


def main():
    DERICTORY = os.getenv("DERICTORY")
    
    photo_list = get_photo_list(DERICTORY)
    random.shuffle(photo_list)
    
    while True:
        for photo_path in photo_list:
            publish_photo(photo_path)
            time.sleep(PUBLISH_DELAY)
        random.shuffle(photo_list)


if __name__ == "__main__":
    main()
    