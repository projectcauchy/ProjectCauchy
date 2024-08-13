import json
from typing import List
from requests import get, Response
from .models import RouletteResponse


def extract(base_url: str, games_count: int = 1) -> List[RouletteResponse]:
    url = f"http://{base_url}:8000/roulette"

    result: List[RouletteResponse] = []
    for _ in range(games_count):
        response: Response = get(url)
        if response.ok:
            result.append(RouletteResponse.from_json(json.dumps(response.json())))

    return result
