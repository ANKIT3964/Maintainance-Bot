# (c) HeimanPictures

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config

@Client.on_message(filters.private & filters.command(['start', 'help', 'about']))
async def start(bot, update):
    await update.reply_text(
        text=Config.MAINTAINANCE_TEXT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("Update Channel", url=https://t.me/defenderofthemultiverse"),
            InlineKeyboardButton("Support Group", url=https://t.me/thewarriorsreal")
            ],[
            InlineKeyboardButton("Repo", url="https://github.com/HeimanPictures/Maintenance-Bot/")
            ]]
        )
    )
