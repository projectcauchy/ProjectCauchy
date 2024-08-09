from .extract import extract
from .transform import transform
from .load import load


def roulette_pipeline(games_count: int = 1):
    roulette_response = extract(games_count)

    roulette_dfs = transform(roulette=roulette_response[0])

    load(roulette_dfs)
