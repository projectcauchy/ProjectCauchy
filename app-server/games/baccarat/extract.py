import json
import requests
import pandas as pd
from tqdm import tqdm


# Temporarily defined get_response here. Should be in utils.py

def get_response(endpoint: str) -> json:
    url = "http://127.0.0.1:8000/" + endpoint
    response = requests.get(url)

    return response.json()


def extract(game: str, n: int) -> list:
    records = []
    for n in tqdm(range(n)):
        response_json = get_response(game)
        records.append(response_json)

    return records