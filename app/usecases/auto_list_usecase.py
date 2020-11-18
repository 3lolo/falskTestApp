import requests
from typing import List

from app.autoria.api.models import RiaParamsBuilder
from app.autoria.api.models.auto_unit import AutoUnit


def load_data(
        last_id: str,
        builder: RiaParamsBuilder,
        ria_api_key: str
) -> List[AutoUnit]:
    ids = _find_ids(last_id, builder, ria_api_key)
    result = []
    for id in ids:
        unit = _get_device_response(ria_api_key, id)
        result.append(unit)
    return result


def _find_ids(
        last_id: str,
        builder: RiaParamsBuilder,
        ria_api_key: str
) -> List[int]:
    api_result = requests.get(f"https://developers.ria.com/auto/search?api_key={ria_api_key}&{builder.build(8)}")
    api_response = api_result.json()
    ids = api_response["result"]["search_result"]["ids"]

    if last_id is not None and last_id in ids:
        index = ids.index(last_id)
        ids = ids[:index]

    return ids


def _get_device_response(ria_api_key, auto_id) -> AutoUnit:
    api_result = requests.get(f"https://developers.ria.com/auto/info?api_key={ria_api_key}&auto_id={auto_id}")
    return AutoUnit.parseJson(api_result.json())
    # return api_result.text
