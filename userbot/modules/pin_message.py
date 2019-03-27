from telethon import events, sync, errors
from telethon.tl import functions as f, types as t
import inspect
import os


@bot.on(events.NewMessage(pattern=r"\.cpin", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    if event.message.reply_to_msg_id is not None:
        message_id = event.message.reply_to_msg_id
        try:
            await bot(f.channels.UpdatePinnedMessageRequest(event.chat_id, message_id, False))
        except Exception as e:
            await event.edit(str(e))
    else:
        await event.edit("Reply to a message to pin the message in this Channel.")
