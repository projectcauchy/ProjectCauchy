from .extract import extract
from .transform import transform
from .load import load


def roulette_pipeline(base_url: str, games_count: int = 1):
    roulette_response = extract(base_url=base_url, games_count=games_count)

    roulette_dfs = transform(roulette_games=roulette_response)

    load(roulette_dfs)
