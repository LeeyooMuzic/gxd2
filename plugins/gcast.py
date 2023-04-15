# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 (C) 2023 𝑩𝒚 @Groot_Network @RJbr0

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from grootxd.clientbot.clientbot import client as aditya
from grootxd.config import SUDO_USERS

@Client.on_message(filters.command(["gcast", "grootcast", "broadcast"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("**`🥀 𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗚𝗿𝗼𝗼𝘁 𝗠𝘂𝘀𝗶𝗰 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁...`**")
        if not message.reply_to_message:
            await wtf.edit("**🎸 𝗣𝗹𝗲𝗮𝘀𝗲 𝗥𝗲𝗽𝗹𝘆 𝗧𝗼 𝗔 𝗠𝗲𝘀𝘀𝗮𝗴𝗲...**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"**🥀 𝗕𝗿𝗼𝗮𝗱𝗰𝗮𝘀𝘁𝗶𝗻𝗴 ...** \n\n**✔️ 𝗦𝗲𝗻𝘁 𝗧𝗼:** `{sent}` **𝗖𝗵𝗮𝘁𝘀** \n**❌ 𝗙𝗮𝗶𝗹𝗲𝗱 𝗜𝗻:** `{failed}` **𝗖𝗵𝗮𝘁𝘀**")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await wtf.delete()
        await message.reply_text(f"**🥀 𝗚𝗰𝗮𝘀𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 ...**\n\n**✔️ 𝗦𝗲𝗻𝘁 𝗧𝗼:** `{sent}` **𝗖𝗵𝗮𝘁𝘀**\n**❌ 𝗙𝗮𝗶𝗹𝗲𝗱 𝗜𝗻:** `{failed}` **𝗖𝗵𝗮𝘁𝘀**")
