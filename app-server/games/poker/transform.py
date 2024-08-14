import pandas as pd
import time
from typing import List, Tuple, Dict, Any
from .poker_logging_config import logger


def transform_data(
    data: List[Dict[str, Any]]
) -> Tuple[
    pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame
]:
    logger.info(f"Starting transformation for {len(data)} games.")
    start_time = time.time()
    transformed_games = []
    transformed_players = []
    transformed_game_players = []
    transformed_community_cards = []
    transformed_hole_cards = []

    try:
        for game in data:
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

            players_df = pd.DataFrame([{
                'playerID': player['playerId'],
                'createdAt': pd.Timestamp.now(),
                'updatedAt': pd.Timestamp.now(),
            } for player in game['players']])
            transformed_players.append(players_df)

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

            hole_cards_df = pd.DataFrame([{
                'GamePlayerID': index,
                'cardRank_1': player['holeCards'][0]['rank'],
                'suit_1': player['holeCards'][0]['suit'],
                'cardRank_2': player['holeCards'][1]['rank'],
                'suit_2': player['holeCards'][1]['suit'],
                'createdAt': pd.Timestamp.now(),
                'updatedAt': pd.Timestamp.now(),
            } for index, player in enumerate(game['players'])])
            transformed_hole_cards.append(hole_cards_df)

        games_df = pd.concat(transformed_games, ignore_index=True)
        players_df = pd.concat(transformed_players, ignore_index=True)
        game_players_df = pd.concat(transformed_game_players, ignore_index=True)
        community_cards_df = pd.concat(transformed_community_cards, ignore_index=True)
        hole_cards_df = pd.concat(transformed_hole_cards, ignore_index=True)
        elapsed_time = time.time() - start_time
        logger.info(f"Transformation took {elapsed_time:.2f} seconds.")

        return games_df, players_df, game_players_df, community_cards_df, hole_cards_df

    except KeyError as e:
        logger.error(f"Missing expected key: {e}")
        raise
    except Exception as e:
        logger.error(f"An error occurred during transformation: {e}")
        raise
