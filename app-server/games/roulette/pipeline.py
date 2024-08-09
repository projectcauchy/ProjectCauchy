from .extract import extract
from .transform import transform
from .load import load


def roulette_pipeline():
    roulette_response = extract()

    roulette_dfs = transform(roulette=roulette_response)

    load(roulette_dfs)
