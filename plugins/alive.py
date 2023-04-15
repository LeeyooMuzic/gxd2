import asyncio
from time import time
from datetime import datetime
from grootxd.config import BOT_IMAGE, BOT_USERNAME, OWNER_USERNAME, UPDATES_CHANNEL, SUPPORT_GROUP, SOURCE_CODE
from grootxd.helpers.filters import command
from grootxd.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""**
┏━❥❥━────➸➽♦️❥❥━────➸➽
┃
┃😇 𝗛𝗶.! 𝗧𝗵𝗶𝘀 𝗜𝘀 𝗚-𝗡𝗘𝗧𝗪𝗢𝗥𝗞 𝗠𝘂𝘀𝗶𝗰
┃ 
┃➪ 𝗔 𝗦𝘂𝗽𝗲𝗿𝗙𝗮𝘀𝘁 𝗛𝗶𝗴𝗵 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 
┃    𝗔𝗻𝗱 𝗪𝗶𝘁𝗵 𝗢𝘂𝘁 𝗟𝗮𝗴 
┃ 𝗣𝗼𝘄𝗲𝗿𝗳𝘂𝗹 𝗠𝘂𝘀𝗶𝗰 𝗣𝗹𝗮𝘆𝗲𝗿 𝗕𝗼𝘁.
┃ 
┃➪ 𝗝𝘂𝘀𝘁 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 𝗮𝗻𝗱 
┃ 𝗘𝗻𝗷𝗼𝘆 𝗦𝘂𝗽𝗲𝗿 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗠𝘂𝘀𝗶𝗰.
┃  
┗━❥❥━────➸➽♦️❥❥━────➸➽**""",
    reply_markup=InlineKeyboardMarkup(
           [[
           InlineKeyboardButton("🌱❰𝗚𝗿𝗼𝗼𝘁 𝗡𝗲𝘁𝘄𝗼𝗿𝗸❱🌱", url=f"https://t.me/Groot_Network"),
           ],[
           InlineKeyboardButton("🌺❰𝗨𝗽𝗱𝗮𝘁𝗲𝘀❱", url="https://t.me/RJbr0"),  
           InlineKeyboardButton("❰𝗢𝘄𝗻𝗲𝗿❱💐", url="https://t.me/SarkarRobot"),
           ],[
           InlineKeyboardButton("🥀❰𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗼𝗱𝗲❱🥀", url="https://github.com/LeeyooMuzicBot/PriyaMusic")
           ]]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive", "#sarkar", "#groot"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 🌱 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗖𝗵𝗮𝘁 𝗚𝗿𝗼𝘂𝗽", url=f"{SUPPORT_GROUP}")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "groot", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph//file/6fbc6c7bfa7af3204f2c1.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😒 𝗜𝘁'𝘀 𝗠𝗲 ", url=f"(https://t.me/rjbr0)")
                ]
            ]
        ),
    )
