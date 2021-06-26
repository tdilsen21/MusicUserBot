# RoBotlarimTg - MusicUserBot
# Burdan hər hansı modulu kodu faylı reponu
# Kopyalayan peysərdi..!!!!
# Sahib - @aykhan_s
     
import sys 
import time
import logging
from pyrogram import Client as mapple, idle
from ᴋɪʀᴀ_ʟɪɢʜᴛ.pyro_auth import Li
from ɴᴏᴛᴇʙᴏᴏᴋ.design_i import *
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
API_ID = Li.API_ID
API_HASH = Li.API_HASH
SESSION_NAME = Li.SESSION_NAME
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
#enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("__ʀʏʊӄi__.txt"),
    logging.StreamHandler()
    ],
    #level=logging.INFO,
)

"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
PLUGINS = dict(
    root="ᴅᴇᴀᴛʜ_ʙᴏᴏᴋ"
)
"""
 \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ /  \ \____/ / 
 / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \__/ / __ \ \_
"""
ʍǟֆȶɛʀʍɨռɖ = mapple(
    session_name=SESSION_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=PLUGINS,
    workers=20
    )
ʍǟֆȶɛʀʍɨռɖ.start()
print("\n\n\n\MeftunMusik'ten izin istiyorum, lütfen dur!\n")
time.sleep(5)
print("Tüm belgeler kontrol edildi!")
time.sleep(3)
print("Senkronize ediliyor")
print("Bitti! .... devam ediyoruz\n")
time.sleep(1)
print("MODUL dosyaları kontrol ediliyor")
time.sleep(1)
print("Senkronize ediliyor!")
time.sleep(3)
print("Bitti!....Başlayalım:\n")
print("                         3")
time.sleep(1)
print("                         2")
time.sleep(1)
print("                         1")
print('✅ MeftunMüzik Oynatılıyor\n')
print(DES_ME)
idle()
ʍǟֆȶɛʀʍɨռɖ.stop()
print("Təmizleme tamamlandı..\n\n\nbot çıkıyor:\n")
time.sleep(1)
print("               1")
time.sleep(1)
print("               2")
time.sleep(1)
print("               3\n\n\n")
print('❌ MeftunMüzik Çevrimdışı\n')
print(DED_ME)
