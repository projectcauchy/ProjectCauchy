import json
import requests
import pandas as pd
from tqdm import tqdm


def extract(url:str) -> json:
    resp = requests.get(f"http://{url}:8000/baccarat")
    resp = resp.json()
    return resp