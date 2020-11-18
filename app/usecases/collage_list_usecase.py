import time
from io import BytesIO

import requests
from PIL import Image, ImageFont, ImageDraw


def createCollage(result: list) -> str or None:
    if len(result) == 0:
        return None
    img_height = 0
    img_width = 0
    collage = Image.new('RGB', (10, 10), (250, 250, 250))

    columns = 2
    rows = int((len(result) - 1) / columns) + 1

    draw = None
    font = ImageFont.truetype('arial.ttf', 72)

    for index, unit in enumerate(result):
        response = requests.get(unit.photo_data)
        img = Image.open(BytesIO(response.content))
        if index == 0:
            img_width, img_height = img.size[0], img.size[1]
            collage = Image.new('RGB', (columns * img_width, rows * img_height), (250, 250, 250))
            draw = ImageDraw.Draw(collage)

        column = index % columns
        row = int(index / columns)
        w, h = font.getsize(f"{index + 1}")
        x, y = img_width * column, img_height * row

        collage.paste(img, (x, y))

        draw.rectangle((x, y, x + w + 10, y + h + 10), fill='black')
        draw.text((img_width * column, img_height * row), f"{index + 1}", font=font)

    id = f"collage_{int(round(time.time() * 1000))}.JPEG"
    path = f"resources/images/{id}"
    collage.save(f"app/{path}", "JPEG")
    return f"app/{path}"
