# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 (C) 2023 𝑩𝒚 @Groot_Network @RJbr0

import os
from pyrogram import Client, filters
from pyrogram.types import Message
from grootxd.helpers.filters import command, other_filters
from grootxd.helpers.decorators import sudo_users_only, errors

downloads = os.path.realpath("downloads")
raw_files = os.path.realpath("raw_files")

@Client.on_message(command(["rmd", "clear"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    ls_dir = os.listdir(downloads)
    if ls_dir:
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **𝗗𝗲𝗹𝗲𝘁𝗲𝗱 𝗔𝗹𝗹 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝗙𝗶𝗹𝗲𝘀...**")
    else:
        await message.reply_text("❌ **𝗡𝗼 𝗙𝗶𝗹𝗲𝘀 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱...**")

        
@Client.on_message(command(["rmr", "clean"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_raw(_, message: Message):
    ls_dir = os.listdir(raw_files)
    if ls_dir:
        for file in os.listdir(raw_files):
            os.remove(os.path.join(raw_files, file))
        await message.reply_text("✅ **𝗗𝗲𝗹𝗲𝘁𝗲𝗱 𝗔𝗹𝗹 𝗥𝗮𝘄 𝗙𝗶𝗹𝗲𝘀...**")
    else:
        await message.reply_text("❌ **𝗡𝗼 𝗥𝗮𝘄 𝗙𝗶𝗹𝗲𝘀 𝗜𝗻 𝗦𝗲𝗿𝘃𝗲𝗿...**")


@Client.on_message(command(["cleanup"]) & ~filters.edited)
@errors
@sudo_users_only
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **𝗖𝗹𝗲𝗮𝗻𝗲𝗱 𝗔𝗹𝗹 𝗝𝘂𝗻𝗸𝘀 𝗧𝗵𝘂𝗺𝗻𝗮𝗶𝗹𝘀...**")
    else:
        await message.reply_text("✅ **𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗖𝗹𝗲𝗮𝗻𝗲𝗱 𝗔𝗹𝗹 𝗝𝘂𝗻𝗸𝘀...**")
