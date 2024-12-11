import telegram
from dotenv import load_dotenv
import os

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN") 


bot = telegram.Bot(token=BOT_TOKEN)
print(bot.get_me())
bot.send_message(chat_id="@CosmoPhotoGroup", text="I'm sorry Dave I'm afraid I can't do that.")