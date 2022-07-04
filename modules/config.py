# 𝗠𝗼𝗱𝘂𝗹𝗲𝘀 𝗮𝗻𝗱 𝗘𝗻𝘃𝗶𝗿𝗼𝗻𝗺𝗲𝗻𝘁𝘀 
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝗜𝗻𝘁𝗲𝗿𝗻𝗮𝗹 𝗩𝗮𝗿𝗶𝗮𝗯𝗹𝗲𝘀 (@𝗚𝗿𝗼𝗼𝘁_𝗡𝗲𝘁𝘄𝗼𝗿𝗸 @𝗠𝘆𝗡𝗮𝗺𝗲𝗜𝘀𝗚𝗿𝗼𝗼𝘁)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝗥𝗲𝗾𝘂𝗶𝗿𝗲𝗱 𝗩𝗮𝗿𝗶𝗮𝗯𝗹𝗲𝘀 //🌱𝗢𝘄𝗻𝗲𝗿 @𝗚𝗿𝗼𝗼𝘁_𝗡𝗲𝘁𝘄𝗼𝗿𝗸 @𝗠𝘆𝗡𝗮𝗺𝗲𝗜𝘀𝗚𝗿𝗼𝗼𝘁
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/b9046390e87cbc3c5b6f0.jpg")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
MONGODB_URL = getenv("MONGODB_URL", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
OWNER_NAME = getenv("OWNER_NAME", "𝗜𝗮𝗺 𝗚𝗿𝗼𝗼𝘁")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Groot_Network")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/rjbr0")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5342963115").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/groot_network")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/rjbr0")

# 𝗗𝗼 𝗡𝗼𝘁 𝗖𝗵𝗮𝗻𝗴𝗲 𝗧𝗵𝗶𝘀 𝗟𝗶𝗻𝗲𝘀 // 𝗜𝗴𝗻𝗼𝗿𝗲 𝗧𝗵𝗶𝘀 (𝗜𝗮𝗺 𝗚𝗿𝗼𝗼𝘁) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/rjbr0")
