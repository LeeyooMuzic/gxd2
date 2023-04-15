from pyrogram import idle
from grootxd.clientbot import run
from pyrogram import Client as Bot
from grootxd.clientbot.clientbot import client
from grootxd.config import API_ID, API_HASH, BOT_TOKEN

    
bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

with Bot(":bgt:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with client as app:
    me_user = app.get_me()
