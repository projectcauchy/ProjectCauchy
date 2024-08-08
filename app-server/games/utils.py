import json
import requests


def get_response(endpoint: str) -> json:
    url = "http://127.0.0.1:8000/" + endpoint
    response = requests.get(url)
    return response.json()