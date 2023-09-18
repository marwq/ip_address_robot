from os import environ

from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = environ['BOT_TOKEN']
IPINFO_TOKEN = environ['IPINFO_TOKEN']
CHAT_ID = environ['CHAT_ID']