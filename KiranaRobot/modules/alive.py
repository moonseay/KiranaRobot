import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from KiranaRobot.events import register
from KiranaRobot import telethn as tbot


PHOTO = "https://graph.org/file/6a3741cd26afbea87d140.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Kirana Robot.** \n\n"
  TEXT += "βͺ **I'm Working Properly** \n\n"
  TEXT += f"βͺ **My Master : [π΄π¦π’ π¬πͺπΊπ°πΈπ°](https://t.me/moonseay)** \n\n"
  TEXT += f"βͺ **Library Version :** `{telever}` \n\n"
  TEXT += f"βͺ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"βͺ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here β€οΈ**"
  BUTTON = [[Button.url("Help", "https://t.me/kiranaxrobot?start=help"), Button.url("Support", "https://t.me/kiranasupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
