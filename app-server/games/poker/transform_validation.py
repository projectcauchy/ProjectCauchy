import pandas as pd
from .poker_logging_config import logger


def validate_dataframes(
    games_df: pd.DataFrame,
    players_df: pd.DataFrame,
    game_players_df: pd.DataFrame,
    community_cards_df: pd.DataFrame,
    hole_cards_df: pd.DataFrame
) -> bool:
    validation_passed = True

    if games_df.empty:
        logger.error("Games DataFrame is empty.")
        validation_passed = False

    if players_df.empty:
        logger.error("Players DataFrame is empty.")
        validation_passed = False

    if game_players_df.empty:
        logger.error("GamePlayers DataFrame is empty.")
        validation_passed = False

    if community_cards_df.empty:
        logger.error("CommunityCards DataFrame is empty.")
        validation_passed = False

    if hole_cards_df.empty:
        logger.error("HoleCards DataFrame is empty.")
        validation_passed = False

    required_columns = {
        "games_df": ['gameID', 'datetime_start', 'datetime_end', 'dealerID', 'winnerID'],
        "players_df": ['playerID'],
        "game_players_df": ['gameID', 'playerID', 'startingChips', 'bestHand', 'netWin'],
        "community_cards_df": ['gameID', 'flopRank', 'flopSuit', 'turnRank', 'turnSuit', 'riverRank', 'riverSuit'],
        "hole_cards_df": ['GamePlayerID', 'cardRank_1', 'suit_1', 'cardRank_2', 'suit_2']
    }

    for df_name, columns in required_columns.items():
        df = locals()[df_name]
        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
            logger.error(f"{df_name} is missing required columns: {missing_columns}")
            validation_passed = False

    critical_columns = {
        "games_df": ['gameID', 'datetime_start', 'datetime_end', 'dealerID', 'winnerID'],
        "players_df": ['playerID'],
        "game_players_df": ['gameID', 'playerID'],
        "community_cards_df": ['gameID'],
        "hole_cards_df": ['GamePlayerID']
    }

    for df_name, columns in critical_columns.items():
        df = locals()[df_name]
        for col in columns:
            if df[col].isnull().any():
                logger.error(f"Missing values found in column {col} of {df_name}.")
                validation_passed = False

    if not set(game_players_df['gameID']).issubset(set(games_df['gameID'])):
        logger.error("Check failed: Some gameIDs in GamePlayers are not present in Games.")
        validation_passed = False

    if not set(game_players_df['playerID']).issubset(set(players_df['playerID'])):
        logger.error("Check failed: Some playerIDs in GamePlayers are not present in Players.")
        validation_passed = False

    if not set(community_cards_df['gameID']).issubset(set(games_df['gameID'])):
        logger.error("Check failed: Some gameIDs in CommunityCards are not present in Games.")
        validation_passed = False

    if not set(hole_cards_df['GamePlayerID']).issubset(set(game_players_df.index)):
        logger.error("Check failed: Some GamePlayerIDs in HoleCards are not present in GamePlayers.")
        validation_passed = False

    return validation_passed
