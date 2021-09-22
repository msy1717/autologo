  

import os, asyncio
os.system("pip install Telethon==1.21.1")

from telethon import TelegramClient, events, functions, types

os.system("pip install Telethon==1.21.1")

api_id = os.environ.get("APP_ID")



from os import system

api_hash = os.environ.get("API_HASH")

token = os.environ.get("BOT_TOKEN")

client = TelegramClient('mrunal', api_id, api_hash).start(bot_token=token)
from telethon import events, Button
import os 
from PIL import Image, ImageDraw, ImageFont
import shutil 
import random, re
import glob
import time
from telethon.tl.types import InputMessagesFilterPhotos

BGS = ["resources/11.jpg", 
       "resources/12.jpg", 
       "resources/13.jpg", 
       "resources/15.jpg"
      ]
 
                         
                         

@client.on(events.NewMessage(incoming=True, pattern="/logo"))
async def lego(event):
 quew = event.text.split("",1)[1]
 #quew = event.text.split[1]
 if not quew:
    await event.reply('Provide Some Text To Draw!')
    return
 else:
    pass
 await event.reply('Creating your logo...wait!')
 try:
    text = event.text.split(" ",1)[1]
    #img = Image.open('./TelethonBot/resources/bgsrnd/15.jpg')
    #dirr = os.listdir("./TelethonBot/resources/bgsrnd")
    #rnd = random.choice(dirr)
    pp = random.choice(BGS)
    img = Image.open(pp)
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    pointsize = 500
    fillcolor = "gold"
    shadowcolor = "blue"
    font = ImageFont.truetype("resources/Chopsic.otf", 330)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    image_width, image_height = img.size
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=25, stroke_fill="yellow")
    fname2 = "LogoBy.png"
    img.save(fname2, "png")
    await client.send_file(event.chat_id, fname2, caption="Made By LoGo Maker Bot")
    if os.path.exists(fname2):
            os.remove(fname2)
 except Exception as e:
   await event.reply(f'Error Report @Godmrunal, {e}')
