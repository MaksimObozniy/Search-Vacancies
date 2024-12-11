from dotenv import load_dotenv
import os

def get_api_key(env_var_name="YOUR_NASA_API_KEY"):
    load_dotenv()
    return os.getenv(env_var_name)