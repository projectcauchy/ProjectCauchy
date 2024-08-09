import json
from typing import List
from requests import get, Response
from .models import RouletteResponse


def extract(games_count: int = 1) -> List[RouletteResponse]:
    base_url: str = "http://127.0.0.1:8000"
    path: str = "/roulette"

    url = base_url + path

    result: List[RouletteResponse] = []
    for _ in range(games_count):
        response: Response = get(url)
        if response.ok:
            result.append(RouletteResponse.from_json(json.dumps(response.json())))

    return result
