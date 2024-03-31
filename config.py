import os
import pyrogram 
import time
import pyrogram
from pyrogram import Client
from pyrogram import enums
import re
import logging
import logging.config
import requests
import logging
from dotenv import load_dotenv
logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

LOGGER = logging

botStartTime2 = time.time()
if os.path.exists('config.env'):
    load_dotenv('config.env')

id_pattern = re.compile(r'^.\d+$') 

def is_enabled(value:str):
    return bool(str(value).lower() in ["true", "1", "e", "d"])

def get_config_from_url():
    CONFIG_FILE_URL = os.environ.get('CONFIG_FILE_URL', None)
    try:
        if len(CONFIG_FILE_URL) == 0: raise TypeError
        try:
            res = requests.get(CONFIG_FILE_URL)
            if res.status_code == 200:
                LOGGER.info("Config uzaktan alındı. Status 200.")
                with open('config.env', 'wb+') as f:
                    f.write(res.content)
                    f.close()
            else:
                LOGGER.error(f"Failed to download config.env {res.status_code}")
        except Exception as e:
            LOGGER.error(f"CONFIG_FILE_URL: {e}")
    except TypeError:
        pass

get_config_from_url()
if os.path.exists('config.env'): load_dotenv('config.env')

id_pattern = re.compile(r'^.\d+$')

LOGGER.info("--- CONFIGS STARTS HERE ---")


botStartTime2 = time.time()

class Config:

    APP_ID = os.environ.get("APP_ID", "7499231")
    API_HASH = os.environ.get("API_HASH", "11aa5d55ab4fb3338d501e1ba276f061")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BABG6QqW9xboAa4qBTWTA-npQbsWTaLW7KtjMPxL2dCFxrXRjbt-BSedqTnphI6aqj4Qij8t6ovf17iVsH0YeF5FO6NS_nnTHgi7YpI3YvkQOji5BS-IrO74IisC2t_Oh8O-wX8WK0r-JCRyjD2PdHrt_w1GkAO0SgCZHWFhwe0HbEtTwSIjCQFd_0gZ1su_IOGDis2FSOGXizLvqsQMbF6O9Z-PzZUuXoJKJcx3VhCf5LxLtzwNebKsBK8xuD_hrBqzK1ATTinshtVdnaU1coT6ObglKp6xG0BQwFcb90qmItpjAXUkaGYxfWGvlbAktRuiJVL7vm05GC4mFXwFvYDJAAAAAVOc0UkA")
    OWNER_ID = os.environ.get("OWNER_ID", 'ahmet118') 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001825274905"))
    KANAL = int(os.environ.get("KANAL", "-1001825274905"))
    SESSION_NAME = os.environ.get("SESSION_NAME", "dizi")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://hplatformss:hplatformss@cluster0.chcsk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", "-1001905375299"))
    OWNERS = list(set(x for x in os.environ.get("OWNERS", "ahmet118").split()))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "diziadmin")
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    SAVE_USER = "yes" 
