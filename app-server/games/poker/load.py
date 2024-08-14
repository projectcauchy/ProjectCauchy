import os
import pandas as pd
from .poker_logging_config import logger


def save_dataframes(games_df: pd.DataFrame, players_df: pd.DataFrame, game_players_df: pd.DataFrame,
                    community_cards_df: pd.DataFrame, hole_cards_df: pd.DataFrame,
                    output_dir: str = 'poker_csv') -> None:
    os.makedirs(output_dir, exist_ok=True)
    games_df.to_csv(f'{output_dir}/games.csv', index=False)
    players_df.to_csv(f'{output_dir}/players.csv', index=False)
    game_players_df.to_csv(f'{output_dir}/game_players.csv', index=False)
    community_cards_df.to_csv(f'{output_dir}/community_cards.csv', index=False)
    hole_cards_df.to_csv(f'{output_dir}/hole_cards.csv', index=False)
    logger.info(f"DataFrames saved to ./{output_dir}.")
