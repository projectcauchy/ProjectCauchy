from typing import Optional
from .extract import extract
from .transform import transform
from .load import load


def blackjack_pipeline(
    players: Optional[int] = None,
    games: Optional[int] = None,
):

    blackjack_response = extract(
        games=games,
        players=players,
    )

    data_frames = transform(blackjack_response)

    load(data_frames)
