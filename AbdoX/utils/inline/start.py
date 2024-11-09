from pyrogram.types import InlineKeyboardButton

import config
from AbdoX import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="𝗦𝗢𝗨𝗥𝗖𝗘 𝗘𝗫𝗣𝗥𝗘𝗦𝗦", url=f"https://t.me/SourceExpress") ,
            InlineKeyboardButton(text="𝗚𝗥𝗢𝗨𝗣", url= "https://t.me/X_v_C_Y"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝚇𝙿𝚁𝙴𝚂𝚂", url=f"https://t.me/expressource"),
            InlineKeyboardButton(text="𝗚𝗥𝗢𝗨𝗣", url=f"https://t.me/X_v_C_Y"), 
        ],
        [
            
            InlineKeyboardButton(text="𝗦𝗢𝗨𝗥𝗖𝗘 𝗘𝗫𝗣𝗥𝗘𝗦𝗦", url=f"https://t.me/SourceExpress") , 
        ],
    ]
    return buttons
