from .paste import create_paste
from pyrogram.types import *
from config import FSUB_ID
from .fsubb import not_subscribed
from pyrogram import Client, filters
from HorridAPI import Mango

@Client.on_message(filters.command("gemma"))
async def gemma_chat(client, message):
    if FSUB_ID and not await not_subscribed(client, message):
        invite_link = await client.create_chat_invite_link(int(FSUB_ID))
        buttons = [[InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ", url=invite_link)]]
        text = f"Hey {message.from_user.mention}\n You are not joined this channel"
        await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
        return 
    if len(message.command) < 2:
        return await message.reply_text("Please provide the query")
        
    query = " ".join(message.command[1:])
    msg = await message.reply_text("🔍")
    mango = Mango()
    response = mango.chat.completions.create(
        model="gemma-2",
        messages=[{"role": "user", "content": query}]
    )
    if len(response.text) > 3700:        
        result = await create_paste(response.text)  
        await msg.edit(result["url"])       
    else:
        await msg.edit(response.text)
