import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 21793031))

    API_HASH = os.environ.get("API_HASH", "52e91180e35e6d91898764b43c567493")
    
    BOT_USER = os.environ.get("BOT_USER", "")
    
    USER_ID = os.environ.get("USER_ID", "")
