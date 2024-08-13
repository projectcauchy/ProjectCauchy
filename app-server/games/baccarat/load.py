from datetime import datetime
from .transform import GameData


def load(game_data: GameData):
    # TODO: Replace with code to load data into prod_db
    
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    game_data.game.to_csv(f"data/baccarat_game_table_{now}.csv",index=False)
    game_data.player_hand.to_csv(f"data/baccarat_player_hand_table_{now}.csv",index=False)
    game_data.banker_hand.to_csv(f"data/baccarat_banker_hand_table_{now}.csv",index=False)
    game_data.hand_value.to_csv(f"data/baccarat_hand_value_table_{now}.csv",index=False)
    game_data.transaction.to_csv(f"data/baccarat_transaction_table_{now}.csv",index=False)