from typing import Optional
from requests import get, Response
from .models import BlackJackResponse


def extract(
    base_url: str,
    players: Optional[int] = None,
    games: Optional[int] = None,
) -> BlackJackResponse:
    url = f"http://{base_url}:8000/blackjack"

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
