#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👨‍💻 𝘋𝘦𝘷𝘭𝘰𝘱𝘦𝘳 :</b> <a href='https://t.me/zorosan110'>Roronoa Zoro</a> \n<b> 🤖 𝘊𝘳𝘦𝘢𝘵𝘰𝘳 :</b> <a href='t.me/InkaLinks'> ᴄʜɪᴘs</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pas
