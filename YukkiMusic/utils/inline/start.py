from pyrogram.types import InlineKeyboardButton

import config
from YukkiMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴧᴅᴅ мᴇ ʙᴧʙʏ", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴧᴅᴅ мᴇ ʙᴧʙʏ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text="sᴜᴘᴘᴏꝛᴛ", url=config.SUPPORT_CHAT),
        ],
        [InlineKeyboardButton(text="ʜᴇʟᴘ ᴧиᴅ ᴄᴏᴍᴍᴧɴᴅs", callback_data="settings_back_helper")],
    ]
    return buttons


def alive_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✿︎ ᴀᴅᴅ ᴍᴇ ✿︎", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
        ],
    ]
    return buttons
