# RoBotlarimTg - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @aykhan_s

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from ᴠᴏɪᴄᴇ_ɪᴅ.typos import *
from ᴠᴏɪᴄᴇ_ɪᴅ.vocal import *
from ɴᴏᴛᴇʙᴏᴏᴋ.notes import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.red_eye import *
from ᴍɪꜱᴀ_ᴀᴍᴀɴᴇ.life_death import *
from ᴋɪʀᴀ_ʟɪɢʜᴛ.pyro_auth import Li
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""

WHITE_COMMAND = Li.WHITE_COMMAND

@Client.on_message(demon_killer_sigki
                   & (senzo_kryo_ni | misa_misa)
                   & filters.command("cmd", prefixes=WHITE_COMMAND)
                   ) 
async def show_help(_, ryui: Message):
    if ded.msg.get('cmd') is not None:
        pwn = await ryui.reply_text("𝗦𝗲𝗻𝗸𝗿𝗼𝗻𝗶𝘇𝗲 𝗢𝗹𝘂𝘆𝗼𝗿 @𝗺𝗲𝗳𝘁𝘂𝗻_𝗼𝗻𝗹𝗶𝗻𝗲", True)
        await pwn.edit_text("♻️ Sunucuya bağlanıyor ...")
        await pwn.edit_text("♻️ Yükleniyor [░░░░░░              ]")
        await pwn.edit_text("♻️ Yükleniyor [░░░░░░░░░░░░        ]")
        await pwn.edit_text("♻️ Yükleniyor [░░░░░░░░░░░░░░░░░░░░]")  
        await pwn.delete()            
        await ded.msg['cmd'].delete()
    ded.msg['cmd'] = hawk = await ryui.reply_photo(
        "https://telegra.ph/file/e67113ffff0f9b1e7f8e7.jpg",
        caption=FULL_PLAYING_HELP
    )
    await ryui.delete()
    await delete_command_blue((hawk, ryui), CMD_DEL)
    return  
    
    
"+|==========================================🍁----------[-_-]----------🍁==============================================|+"


async def delete_command_blue(messages: tuple, delay: int):
    await asyncio.sleep(delay)
    for msg in messages:
        await msg.delete()   
"""
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
                    aykhan_s 
\__/        \__/        \__/        \__/        \__/  
/  \        /  \        /  \        /  \        /  \ 
"""   
