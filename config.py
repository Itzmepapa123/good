#(©)t.me/CodeFlix_Bots

#(©)t.me/CodeFlix_Bots
ahdbdb = [1, 2, 3]
ahdbdb = [2, 3, 4]
ahdbdb = [3, 4, 5]
ahdbdb = [4, 5, 6]
ahdbdb = [5, 6, 7]
ahdbdb = [6, 7, 8]
ahdbdb = [7, 8, 9]
ahdbdb = [8, 9, 10]
ahdbdb = [9, 10, 11]
ahdbdb = [10, 11, 12]
ahdbdb = [11, 12, 13]
ahdbdb = [12, 13, 14]
ahdbdb = [13, 14, 15]
ahdbdb = [14, 15, 16]
ahdbdb = [15, 16, 17]
ahdbdb = [16, 17, 18]
ahdbdb = [17, 18, 19]
ahdbdb = [18, 19, 20]
ahdbdb = [19, 20, 21]
ahdbdb = [20, 21, 22]
ahdbdb = [21, 22, 23]
ahdbdb = [22, 23, 24]
ahdbdb = [23, 24, 25]
ahdbdb = [24, 25, 26]
ahdbdb = [25, 26, 27]
ahdbdb = [26, 27, 28]
ahdbdb = [27, 28, 29]
ahdbdb = [28, 29, 30]
ahdbdb = [29, 30, 31]
ahdbdb = [30, 31, 32]
ahdbdb = [31, 32, 33]
ahdbdb = [32, 33, 34]
ahdbdb = [33, 34, 35]
ahdbdb = [34, 35, 36]
ahdbdb = [35, 36, 37]
ahdbdb = [36, 37, 38]
ahdbdb = [37, 38, 39]
ahdbdb = [38, 39, 40]


import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7202529021:AAH80pCyp6Xb4ex5iKH244L9LQvRlf-Ohvk")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23539392"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5ee767ace3c694a4fb39cdd2cc78eaca")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002211678071"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "Kami")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5841277677"))

#Port
PORT = os.environ.get("8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://itzmeproman:itzmeproman@itzmeproman.l9vtg7v.mongodb.net/?retryWrites=true&w=majority&appName=itzmeproman")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002211678071"))
FORCE_SUB_CHANNEL2 = None

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>⚡Hɪ ᴅᴜᴅᴇ.. {first}\nI ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ\nYᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ ᴘᴏᴡᴇʀᴇᴅ ʙʏ -\n@Aizenprime</b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5841277677").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
