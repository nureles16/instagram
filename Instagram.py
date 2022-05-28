from PIL import Image
from PIL import ImageDraw, ImageFont
import os

files_formats = ['.jpg', '.jpeg', '.png', '.webp']
size_1080 = (1080,1080)

os.mkdir('img')

for x in os.listdir('.'):
    fn, fext = os.path.splitext(x)

    if fext.lower() in files_formats:
        img = Image.open(x)
        img = img.resize(size_1080)
        img = img.convert('L')
        width, height = img.size
        draw = ImageDraw.Draw(img)
        text = "NUR"

        font = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 75)
        textwidth, textheight = draw.textsize(text, font)
        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin
        draw.text((x, y), text, font=font)
        img.save(f'img/{fn}.jpg')