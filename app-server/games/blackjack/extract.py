from typing import Optional
from requests import get, Response
from .models import BlackJackResponse


def extract(
    players: Optional[int] = None,
    games: Optional[int] = None,
) -> BlackJackResponse:
    base_url: str = "http://127.0.0.1:8000"
    path: str = "/blackjack"

    url = base_url + path

    response: Response = get(
        url,
        params={
            "players": players,
            "games": games,
        },
    )

    if response.ok:
        return BlackJackResponse(**response.json())
    else:
        raise Exception(response.json())
