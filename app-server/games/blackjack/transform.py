from dataclasses import asdict
from random import Random
import string
from typing import List, Tuple
import pandas as pd
from models.blackjack_response import BlackJackResponse


def _generate_id() -> str:
    return "".join(
        Random().choices(
            string.ascii_uppercase + string.digits,
            k=6,
        )
    )


def transform(blackjack: BlackJackResponse) -> List[Tuple[str, pd.DataFrame]]:

    game_df: List = []
    dealer_hand_df: List = []
    player_hand_df: List = []
    dealer_dealt_card_df: List = []
    player_dealt_card_df: List = []

    for transaction in blackjack.transactions:
        game_df.append(
            {
                "game_id": transaction.gameId,
                "status": transaction.status,
                "last_action": transaction.lastAction,
                "timestamp": transaction.timestamp,
            }
        )

        dealer_hand_id = _generate_id()
        dealer_hand_df.append(
            {
                "dealer_hand_id": dealer_hand_id,
                "game_id": transaction.gameId,
                "did_win": "dealer wins" in transaction.outcome.lower(),
                "payout": -1 * transaction.payout,
            }
        )

        player_hand_id = _generate_id()
        player_hand_df.append(
            {
                "player_hand_id": player_hand_id,
                "game_id": transaction.gameId,
                "player_id": transaction.player_id,
                "did_win": "player wins" in transaction.outcome.lower(),
                "payout": transaction.payout,
                "player_balance": transaction.playerBalance,
                "current_bet": transaction.currentBet,
            }
        )

        for card in transaction.dealerHand:
            dealer_dealt_card_df.append(
                {
                    "dealt_card_id": _generate_id(),
                    "dealer_hand_id": dealer_hand_id,
                    "card": asdict(card),
                }
            )

        for card in transaction.dealerHand:
            player_dealt_card_df.append(
                {
                    "dealt_card_id": _generate_id(),
                    "player_hand_id": player_hand_id,
                    # Ideally we would have a separate table for cards
                    "card": asdict(card),
                }
            )

    return [
        ("game", pd.DataFrame(game_df)),
        ("dealer_hand", pd.DataFrame(dealer_hand_df)),
        ("player_hand", pd.DataFrame(player_hand_df)),
        ("dealer_dealt_card", pd.DataFrame(dealer_dealt_card_df)),
        ("player_dealt_card", pd.DataFrame(player_dealt_card_df)),
    ]
