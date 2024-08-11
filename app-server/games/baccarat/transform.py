import ast
import json
import string
import random
import pandas as pd
from dataclasses import dataclass



@dataclass
class GameData:
    game: pd.DataFrame
    player_hand: pd.DataFrame
    banker_hand: pd.DataFrame
    hand_value: pd.DataFrame
    transaction: pd.DataFrame



def transform(resp: json) -> pd.DataFrame:
    
    game_details_df = pd.DataFrame([resp])

    game_df = transform_game_data(game_details_df)
    player_hand_df = transform_hand_data(game_details_df, 'player')
    banker_hand_df = transform_hand_data(game_details_df, 'banker')
    hand_value_df = transform_hand_value_data(game_details_df)
    transaction_df = transform_transaction_data(game_details_df)

    return GameData(
        game=game_df,
        player_hand=player_hand_df,
        banker_hand=banker_hand_df,
        hand_value=hand_value_df,
        transaction=transaction_df
    )



def transform_game_data(game_details_df: pd.DataFrame) -> pd.DataFrame:

    game_df_cols = ['game_id', 'game_name', 'status', 
                    'start_time', 'end_time', 'last_action',
                    'player_wager', 'player_payout', 'game_outcome', 
                    'player_bet', 'player_bet_outcome', 'player_id'
                   ]
    game_df = game_details_df[game_df_cols]

    return game_df



def transform_hand_data(game_details_df: pd.DataFrame, hand: str)  -> pd.DataFrame:

    hand = f"{hand}_hand"
    
    game_details_df[hand] = game_details_df[hand].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)
    exploded_df = game_details_df[['game_id', 'player_id', hand]].explode(hand).reset_index(drop=True)
    normalized_df = pd.json_normalize(exploded_df[hand])
    hand_df = pd.concat([exploded_df, normalized_df], axis = 1).drop(columns = [hand])

    return hand_df



def transform_hand_value_data(game_details_df: pd.DataFrame) -> pd.DataFrame:

    hvid = 'HVID' + '-' +''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    hand_value_df = game_details_df[['game_id', 'player_hand_value', 'banker_hand_value']]
    hand_value_df.insert(0, 'hand_value_id', hvid)

    return hand_value_df



def transform_transaction_data(game_details_df: pd.DataFrame) -> pd.DataFrame:

    tid = 'TID' + '-' +''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    transaction_df = game_details_df[['game_id', 'player_id', 'player_wager', 'player_payout', 'end_time']]
    transaction_df = transaction_df.rename(columns = {'end_time':'transaction_time_df'})
    transaction_df.insert(0, 'transaction_id_df', tid)

    return transaction_df