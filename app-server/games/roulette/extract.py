import json
from requests import get, Response
from models import RouletteResponse


def extract() -> RouletteResponse:
    base_url: str = "http://127.0.0.1:8000"
    path: str = "/roulette"

    url = base_url + path

    response: Response = get(url)

    if response.ok:
        return RouletteResponse.from_json(json.dumps(response.json()))
    else:
        raise Exception(response.json())
