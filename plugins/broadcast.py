import asyncio
import traceback

from pyrogram.types import Message
from pyrogram import Client, filters
from grootxd import me_bot
from grootxd.helpers.filters import command
from grootxd.helpers.decorators import errors, sudo_users_only
from grootxd.database.dbchat import get_served_chats
from grootxd.database.dbusers import get_served_users
from grootxd.database.dbpunish import get_gbans_count
from grootxd.database.dbqueue import get_active_chats

from grootxd.config import BOT_USERNAME as uname


@Client.on_message(command(["broadcast", f"broadcast@{uname}"]) & ~filters.edited)
@errors
@sudo_users_only
async def broadcast_message_nopin(c: Client, message: Message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"✅ Broadcast complete in {sent} Group.")
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**usage**:\n\n/broadcast (`message`) or (`reply to message`)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"✅ Broadcast complete in {sent} Group.")


@Client.on_message(command(["broadcast_pin", f"broadcast_pin@{uname}"]) & ~filters.edited)
@errors
@sudo_users_only
async def broadcast_message_pin(c: Client, message: Message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await c.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"✅ Broadcast complete in {sent} Group.\n📌 Sent with {pin} chat pins."
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**usage**:\n\n/broadcast_pin (`message`) or (`reply to message`)"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await c.send_message(i, text=text)
            try:
                await m.pin(disable_notification=True)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(
        f"✅ Broadcast complete in {sent} Group.\n📌 Sent with {pin} chat pins."
    )
