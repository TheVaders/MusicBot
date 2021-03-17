from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f""" 🤩🥳 HELLO {message.from_user.first_name}!

😍 I am Sangram Ghangale Music Player. 

🥳 Sorry I can't play music in your Telegram Group's Voice Chat..

 Use these buttons below to know more. 👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 12TH Study material 📚", url="https://t.me/hscscienceMaharashtraboard"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Chat Group 💬", url="https://t.me/MAHARASHTRAFRIENDS"
                    ),
                    InlineKeyboardButton(
                        "📣 12TH Channel 📣", url="https://t.me/digestnotes"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "**Sangrammusicbot -** I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Search 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
