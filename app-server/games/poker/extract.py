import requests
import logging
import time
from typing import Optional, Any, Dict, List
# from pprint import pprint

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_poker(poker_hands: int = 1) -> Optional[List[Dict[str, Any]]]:
    url: str = f"http://localhost:8000/poker?hands={poker_hands}"

    # Start timing the extraction process
    start_time: float = time.time()
    print("Extraction info:")
    print(f"Extraction source: {url}")
    print(f"Total poker hands: {poker_hands}")

    try:
        response: requests.Response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data: Dict[str, Any] = response.json()

        # Log the successful extraction
        logging.info(f"Successfully extracted {poker_hands} hands of poker data.")
        elapsed_time: float = time.time() - start_time
        logging.info(f"Extraction time: {elapsed_time:.2f} seconds.")

        return data

    except requests.exceptions.RequestException as e:
        # Log errors in extraction
        logging.error(f"Failed to extract data: {e}")
        return None

# result = extract_poker(5)
#
# # Pretty print the result
# if result:
#     pprint(result)
