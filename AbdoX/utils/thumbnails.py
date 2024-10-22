import os
import re

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from youtubesearchpython.__future__ import VideosSearch

from AbdoX import app
from config import YOUTUBE_IMG_URL


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage

async def gen_bot_caesar(client, bot_username, OWNER_ID, CASER, message, videoid):
    if os.path.isfile(f"photos/{videoid}_{bot_username}.png"):
        return f"photos/{videoid}_{bot_username}.png"

    url = f"https://www.youtube.com/watch?v={videoid}"
    try:
        results = VideosSearch(url, limit=1)
        for result in (await results.next())["result"]:
            try:
                title = result["title"]
                title = re.sub("\W+", " ", title)
                title = title.title()
            except:
                title = "Unsupported Title"
            try:
                duration = result["duration"]
            except:
                duration = "Unknown Mins"
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
            try:
                views = result["viewCount"]["short"]
            except:
                views = "Unknown Views"
            try:
                channel = result["channel"]["name"]
            except:
                channel = "Unknown Channel"

        async with aiohttp.ClientSession() as session:
            async with session.get(thumbnail) as resp:
                if resp.status == 200:
                    f = await aiofiles.open(f"thumb{videoid}.png", mode="wb")
                    await f.write(await resp.read())
                    await f.close()

        youtube = Image.open(f"thumb{videoid}.png")
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(10))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.6)
        draw = ImageDraw.Draw(background)
        arial = ImageFont.truetype("font.ttf", 70)
        caesa = ImageFont.truetype("font.ttf", 45)        
        box_size = (500, 500)
        box_position = (40, 100)
        box_image = Image.new("RGBA", box_size, (255, 255, 255, 0))
        box_draw = ImageDraw.Draw(box_image)
        box_draw.ellipse([(0, 0), box_size], outline="white", width=5)               
        wxyz = await client.get_chat(OWNER_ID)
        CAR = wxyz.username
        vvv = wxyz.photo.big_file_id
        wxy = await client.download_media(vvv)
        inner_image = Image.open(wxy)
        inner_image = inner_image.resize((480, 480))
        box_image.paste(inner_image, (10, 10))  
        background.paste(box_image, box_position)   
        draw.text((600, 120), "JaCK PlAYiNg", fill="white", stroke_width=2, stroke_fill="white", font=arial)     
        draw.text((600, 420), f"{channel} | {views[:23]}", (255, 255, 255), font=caesa)        
        draw.text((600, 490), f"Channel : {channel}", (255, 255, 255), font=caesa)       
        draw.text((600, 350), f"Views : {views[:23]}", (255, 255, 255), font=caesa) 
        draw.text((600, 550), f"Duration : {duration[:23]} Mins", (255, 255, 255), font=caesa)    
        background.save(f"photos/{videoid}_{bot_username}.png")
        os.remove(f"thumb{videoid}.png")
        file = f"photos/{videoid}_{bot_username}.png"
        return file
    except Exception as e:
        print(e)
