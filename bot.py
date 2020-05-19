import discord
import pytesseract
import requests
from io import BytesIO
from PIL import Image 

bot = discord.Client()
@bot.event
async def on_ready():
    print('woulajsuilà')

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    if str(msg.channel) == "bot_kovaak" and len(msg.attachments) > 0:
        for attachment in msg.attachments:
            response = requests.get(attachment.url)
            img = Image.open(BytesIO(response.content))
            text = pytesseract.image_to_string(img, lang='eng')
            f = open("ceciestuntexte.txt", "a")
            f.write(text + "\n")
            f.close()



pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different
bot.run('NzExOTcxMjAyMjg5MTA3MDM2.XsKxug.3QSWIlsBYF0xlw3m5l8W4u79w1o')