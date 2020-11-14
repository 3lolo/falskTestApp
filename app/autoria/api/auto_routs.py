# return json.dumps([ob.__dict__ for ob in result])
import json
import time
from io import BytesIO

import flask
import requests
from PIL import Image, ImageDraw, ImageFont

from app.autoria.api import auto_bp
from app.autoria.api.models.RiaParamsBuilder import RiaParamsBuilder
from app.autoria.api.models.auto_unit import AutoUnit
from app.autoria.api.templates.auto_unit_telegram_message import AutoUnitTelegramMessage
from app.repository import IdsRepository


@auto_bp.route('/list', methods=['GET'])
def get_autos_list():
    repository = IdsRepository("app/db/last_ids")
    id = repository.read_id()

    ria_api_key = 'DtjLTYtg3ExFTlmn4FLnsIhCVeU0i5nOIdlaVSce'
    chat_id = '300181845'
    bot_id = '1216317183:AAEkRkYDCLt2NQ-1Mqm9WeJbURHgVsbp14g'
    params_builder = RiaParamsBuilder()
    api_result = requests.get(f"https://developers.ria.com/auto/search?api_key={ria_api_key}&{params_builder.build()}")
    api_response = api_result.json()
    ids = api_response["result"]["search_result"]["ids"]
    result = []
    if id is not None:
        if id in ids:
            index = ids.index(id)
            ids = ids[:index]

    for id in enumerate(ids):
        unit = _get_device_response(ria_api_key, id)
        result.append(unit)

    path = _createCollage(result)
    auto_unit = AutoUnitTelegramMessage(result)
    tg_message = auto_unit.createParamsRequest(chat_id)

    if len(result) > 0:
        repository.save_id(result[0].auto_id)

    if path is not None:
        files = {'photo': open(path, 'rb')}
        params = {
            'chat_id': chat_id,
            'parse_mode': 'HTML'
        }
        requests.post(f"https://api.telegram.org/bot{bot_id}/sendPhoto", files=files, params=params)

    return requests.get(f"https://api.telegram.org/bot{bot_id}/sendMessage?{tg_message}").text


@auto_bp.route('/resources/<id>', methods=['GET'])
def get_resources(id):
    return flask.send_file(f"resources/images/{id}", mimetype="image/JPEG")


@auto_bp.route('', methods=['GET'])
def api_home():
    return "Hello"


@auto_bp.route('write', methods=['GET'])
def _save_last_id(id):
    with open("app/db/last_ids", "r+") as file:
        line = file.readline()
        file.seek(0)
        file.write(f"{id}")
        file.close()

    return line


def _get_device_response(ria_api_key, auto_id):
    api_result = requests.get(f"https://developers.ria.com/auto/info?api_key={ria_api_key}&auto_id={auto_id}")
    return AutoUnit.parseJson(api_result.json())


def _createCollage(result: list) -> str or None:
    if len(result) == 0:
        return None
    img_height = 0
    img_width = 0
    collage = Image.new('RGB', (10, 10), (250, 250, 250))

    columns = 2

    draw = None
    font = ImageFont.truetype('arial.ttf', 72)
    for index, unit in enumerate(result):
        response = requests.get(unit.photo_data)
        img = Image.open(BytesIO(response.content))
        if index == 0:
            img_width = img.size[0]
            img_height = img.size[1]
            collage = Image.new('RGB', (columns * img_width, int(len(result) / columns) * img_height), (250, 250, 250))
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
