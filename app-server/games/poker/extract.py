import requests
import time
import os
from typing import Optional, Any, Dict, List
from dotenv import load_dotenv
from .poker_logging_config import logger

load_dotenv()


def ensure_url_scheme(url: str) -> str:
    if not url.startswith(('http://', 'https://')):
        if ':' not in url.split('/')[0]:
            return f"http://{url}:8000"
        return f"http://{url}"
    return url


def extract_poker(poker_hands: int = 1, env: str = "development") -> Optional[List[Dict[str, Any]]]:
    base_url = os.getenv("PROD_HOST") if env == "production" else os.getenv("DEV_HOST")
    base_url = ensure_url_scheme(base_url)  # Ensure the URL has a scheme
    url: str = f"{base_url}/poker?hands={poker_hands}"
    start_time: float = time.time()

    logger.info("Extraction info:")
    logger.info(f"Extraction source: {url}")
    logger.info(f"Total poker hands: {poker_hands}")

    try:
        response: requests.Response = requests.get(url, timeout=10)
        response.raise_for_status()
        data: List[Dict[str, Any]] = response.json()
        logger.info(f"Successfully extracted {poker_hands} hands of poker data.")
        elapsed_time: float = time.time() - start_time
        logger.info(f"Extraction time: {elapsed_time:.2f} seconds.")

        return data

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to extract data: {e}")
        return None
