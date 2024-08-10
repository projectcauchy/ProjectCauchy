import os
import pandas as pd
import logging
import time
from typing import List, Tuple, Dict, Any, Optional
from extract import extract_poker
from transform_validation import validate_dataframes

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def transform_data(data: List[Dict[str, Any]]) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    logging.info(f"Starting transformation for {len(data)} games.")
    start_time = time.time()

    transformed_games = []
    transformed_players = []
    transformed_game_players = []
    transformed_community_cards = []
    transformed_hole_cards = []

    try:
        for game in data:
            # Games Table
            games_df = pd.DataFrame({
                'gameID': [game['gameID']],
                'datetime_start': [pd.to_datetime(game['datetime_start'])],
                'datetime_end': [pd.to_datetime(game['datetime_end'])],
                'dealerID': [game['employeeDealerId']],
                'winnerID': [game['winner']],
                'rounds': [int(game['totalRounds'])],
                'winType': [game['winType']],
                'totalPot': [float(game['totalPot'])],
                'initialBlind': [float(game['initialBlind'])],
                'rake': [float(game['rake'])],
                'createdAt': [pd.Timestamp.now()],
                'updatedAt': [pd.Timestamp.now()],
            })
            transformed_games.append(games_df)

            # Players Table
            players_df = pd.DataFrame([{
                'playerID': player['playerId'],
                'createdAt': pd.Timestamp.now(),
                'updatedAt': pd.Timestamp.now(),
            } for player in game['players']])
            transformed_players.append(players_df)

            # GamePlayers Table
            game_players_df = pd.DataFrame([{
                'gameID': game['gameID'],
                'playerID': player['playerId'],
                'startingChips': float(player['startingChips']),
                'bestHand': player['bestHand'],
                'netWin': float(player['netWin']),
                'createdAt': pd.Timestamp.now(),
                'updatedAt': pd.Timestamp.now(),
            } for player in game['players']])
            transformed_game_players.append(game_players_df)

            # CommunityCards Table
            community_cards_df = pd.DataFrame({
                'gameID': game['gameID'],
                'flopRank': [card['rank'] for card in game['communityCards']['flop']],
                'flopSuit': [card['suit'] for card in game['communityCards']['flop']],
                'turnRank': game['communityCards']['turn']['rank'],
                'turnSuit': game['communityCards']['turn']['suit'],
                'riverRank': game['communityCards']['river']['rank'],
                'riverSuit': game['communityCards']['river']['suit'],
                'createdAt': pd.Timestamp.now(),
                'updatedAt': pd.Timestamp.now(),
            })
            transformed_community_cards.append(community_cards_df)

            # HoleCards Table
            hole_cards_df = pd.DataFrame([{
                'GamePlayerID': index,  # Placeholder for the FK, should be managed during loading
                'cardRank_1': player['holeCards'][0]['rank'],
                'suit_1': player['holeCards'][0]['suit'],
                'cardRank_2': player['holeCards'][1]['rank'],
                'suit_2': player['holeCards'][1]['suit'],
                'createdAt': pd.Timestamp.now(),
                'updatedAt': pd.Timestamp.now(),
            } for index, player in enumerate(game['players'])])
            transformed_hole_cards.append(hole_cards_df)

        # DataFrame concatenation enable for multiple poker hands
        games_df = pd.concat(transformed_games, ignore_index=True)
        players_df = pd.concat(transformed_players, ignore_index=True)
        game_players_df = pd.concat(transformed_game_players, ignore_index=True)
        community_cards_df = pd.concat(transformed_community_cards, ignore_index=True)
        hole_cards_df = pd.concat(transformed_hole_cards, ignore_index=True)

        elapsed_time = time.time() - start_time
        logging.info(f"Transformation took {elapsed_time:.2f} seconds.")

        return games_df, players_df, game_players_df, community_cards_df, hole_cards_df

    except KeyError as e:
        logging.error(f"Missing expected key: {e}")
        raise
    except Exception as e:
        logging.error(f"An error occurred during transformation: {e}")
        raise


def save_dataframes(games_df: pd.DataFrame, players_df: pd.DataFrame, game_players_df: pd.DataFrame,
                    community_cards_df: pd.DataFrame, hole_cards_df: pd.DataFrame,
                    output_dir: str = 'poker_csv') -> None:
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save DataFrames to CSV files in the specified directory (default = ./poker_csv)
    games_df.to_csv(f'{output_dir}/games.csv', index=False)
    players_df.to_csv(f'{output_dir}/players.csv', index=False)
    game_players_df.to_csv(f'{output_dir}/game_players.csv', index=False)
    community_cards_df.to_csv(f'{output_dir}/community_cards.csv', index=False)
    hole_cards_df.to_csv(f'{output_dir}/hole_cards.csv', index=False)

    # Log the successful saving of the DataFrames
    logging.info(f"DataFrames saved to ./{output_dir}.")
