from typing import Optional
from .extract import extract_poker
from .transform import transform_data
from .load import save_dataframes
from .transform_validation import validate_dataframes
from .poker_logging_config import logger


def poker_pipeline(
    env: str = "development",
    poker_hands: Optional[int] = 1
):
    logger.info("Starting Poker ETL pipeline...")

    data = extract_poker(poker_hands=poker_hands, env=env)
    if not data:
        logger.error("Extraction failed. Pipeline will not proceed.")
        return

    try:
        games_df, players_df, game_players_df, community_cards_df, hole_cards_df = transform_data(data)
    except Exception as e:
        logger.error(f"Transformation failed: {e}")
        return

    if validate_dataframes(games_df, players_df, game_players_df, community_cards_df, hole_cards_df):
        logger.info("Validation passed. Transformation complete.")
        save_dataframes(games_df, players_df, game_players_df, community_cards_df, hole_cards_df)
    else:
        logger.error("Validation failed. DataFrames not saved or processed further.")

    logger.info("Poker ETL pipeline completed.")
