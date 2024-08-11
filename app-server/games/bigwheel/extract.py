import pandas as pd
import requests
import os

def extract(url):
    resp = requests.get(f"http://{url}:8000/bigwheel")
    df = pd.DataFrame(resp.json())
    return df
