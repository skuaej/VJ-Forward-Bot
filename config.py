# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "27479878"))
    API_HASH = environ.get("API_HASH", "05f8dc8265d4c5df6376dded1d71c0ff")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8450047941:AAHVm6UBQ1OYI7Psxmgg0qPAUA5lEquk7kU") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI","mongodb+srv://sumankumar821311_db_user:e6tYVXxhD2jRTRbn@cluster0.dpt7ky6.mongodb.net/aniumeDB?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "vj-forward-bot")
    BOT_OWNER = int(environ.get("BOT_OWNER", "6804892450"))

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
