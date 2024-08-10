import logging
from extract import extract_poker
from transform import transform_data
from transform import save_dataframes
from transform_validation import validate_dataframes


def pipeline_poker(poker_hands: int = 1):
    logging.info("Starting Poker ETL pipeline...")

    # Step 1: Extract
    data = extract_poker(poker_hands)
    if not data:
        logging.error("Extraction failed. Pipeline will not proceed.")
        return

    # Step 2: Transform
    try:
        games_df, players_df, game_players_df, community_cards_df, hole_cards_df = transform_data(data)
    except Exception as e:
        logging.error(f"Transformation failed: {e}")
        return

    # Step 3: Validate
    if validate_dataframes(games_df, players_df, game_players_df, community_cards_df, hole_cards_df):
        logging.info("Validation passed. Transformation complete.")
        save_dataframes(games_df, players_df, game_players_df, community_cards_df, hole_cards_df)
        # Loading to follow
    else:
        logging.error("Validation failed. DataFrames not saved or processed further.")

    logging.info("Poker ETL pipeline completed.")