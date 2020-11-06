from app.autoria.api import auto_bp
from app.autoria.api.models.auto_unit import AutoUnit
import requests
import json

from app.autoria.api.templates.auto_unit_telegram_message import AutoUnitTelegramMessage


@auto_bp.route('/list', methods=['GET'])
def get_autos_list():
    params = "category_id=1&(price_ot=8000&price_do=12000&currency=1&countpage=3"
    ria_api_key = 'DtjLTYtg3ExFTlmn4FLnsIhCVeU0i5nOIdlaVSce'
    chat_id = '300181845'
    bot_id = '1216317183:AAEkRkYDCLt2NQ-1Mqm9WeJbURHgVsbp14g'

    api_result = requests.get(f"https://developers.ria.com/auto/search?api_key={ria_api_key}&{params}")
    api_response = api_result.json()
    ids = api_response["result"]["search_result"]["ids"]
    result = []
    for num, id in enumerate(ids, start=1):
        telegram_message = get_device_response(ria_api_key, id)
        result.append(telegram_message)

    tgMessage = AutoUnitTelegramMessage(result).createParamsRequest(chat_id)
    api_result = requests.get(f"https://api.telegram.org/bot{bot_id}/sendMessage?{tgMessage}")

    return api_result


@auto_bp.route('', methods=['GET'])
def api_home():
    # return json.dumps([ob.__dict__ for ob in result])
    return "Hello"


def get_device_response(ria_api_key, auto_id):
    api_result = requests.get(f"https://developers.ria.com/auto/info?api_key={ria_api_key}&auto_id={auto_id}")
    return AutoUnit.parseJson(api_result.json())
