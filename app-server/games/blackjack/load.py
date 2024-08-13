from typing import List, Tuple
import pandas as pd


def load(data_frames: List[Tuple[str, pd.DataFrame]]):
    for file_name, data_frame in data_frames:
        data_frame.to_csv(f"games/blackjack/data/{file_name}.csv")
