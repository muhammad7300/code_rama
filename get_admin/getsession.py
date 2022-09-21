
from pyrogram import Client
from pyrogram import filters
from pyrogram import idle
from pyrogram import errors

from pyrogram.types import InlineKeyboardButton as button
from pyrogram.types import InlineKeyboardMarkup as markup
from pyrogram.types import ForceReply as reply

api_id, api_hash = 17477721, "ac5b5a696949e9f62336e6997dc9f840"
with Client("session_me",api_id,api_hash) as cli:
        cli.send_message("me","Log in session pyrogram")

            

