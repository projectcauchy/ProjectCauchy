from random import Random
import string
from typing import Dict, List, Tuple
import pandas as pd
from .models import RouletteResponse, SinglePocketBet, OutsideBet


def _generate_id() -> str:
    return "".join(
        Random().choices(
            string.ascii_uppercase + string.digits,
            k=6,
        )
    )


__GAME = "game"
__WINNING_POCKET = "winning_pocket"
__INSIDE_BET = "inside_bet"
__INSIDE_BET_DETAILS = "inside_bet_details"
__DOZEN_BET = "dozen_bet"
__COLUMN_BET = "column_bet"
__ODD_OR_EVEN_BET = "odd_or_even_bet"
__HIGH_OR_LOW_BET = "high_or_low_bet"
__COLOR_BET = "color_bet"


def transform(roulette_games: List[RouletteResponse]) -> List[Tuple[str, pd.DataFrame]]:
    game_df: List = []
    winning_pocket_df: List = []
    inside_bet_df: List = []
    inside_bet_details_df: List = []
    dozen_bet_df: List = []
    column_bet_df: List = []
    odd_or_even_bet_df: List = []
    high_or_low_bet_df: List = []
    color_bet_df: List = []

    for roulette in roulette_games:
        map = _transform_roulette_as_dict(roulette=roulette)
        game_df += map[__GAME]
        winning_pocket_df += map[__WINNING_POCKET]
        inside_bet_df += map[__INSIDE_BET]
        inside_bet_details_df += map[__INSIDE_BET_DETAILS]
        dozen_bet_df += map[__DOZEN_BET]
        column_bet_df += map[__COLUMN_BET]
        odd_or_even_bet_df += map[__ODD_OR_EVEN_BET]
        high_or_low_bet_df += map[__HIGH_OR_LOW_BET]
        color_bet_df += map[__COLOR_BET]

    return [
        (__GAME, pd.DataFrame(game_df)),
        (__WINNING_POCKET, pd.DataFrame(winning_pocket_df)),
        (__INSIDE_BET, pd.DataFrame(inside_bet_df)),
        (__INSIDE_BET_DETAILS, pd.DataFrame(inside_bet_details_df)),
        (__DOZEN_BET, pd.DataFrame(dozen_bet_df)),
        (__COLUMN_BET, pd.DataFrame(column_bet_df)),
        (__ODD_OR_EVEN_BET, pd.DataFrame(odd_or_even_bet_df)),
        (__HIGH_OR_LOW_BET, pd.DataFrame(high_or_low_bet_df)),
        (__COLOR_BET, pd.DataFrame(color_bet_df)),
    ]


def _inside_bet_details(bet_id: str, pocket_number: int) -> Dict:
    return {
        "inside_bet_details_id": _generate_id(),
        "inside_bet_id": bet_id,
        "pocket_number": pocket_number,
    }


def _outside_bet_dict(bet: OutsideBet, bet_type: str) -> Dict:
    return {
        f"{bet_type}_bet_id": bet.id,
        bet_type: bet.bet if bet.bet is not None else bet.type,
        "bet_amount": bet.bet_amount,
        "amount_won": bet.amount_won,
    }


def _transform_roulette_as_dict(roulette: RouletteResponse) -> Dict[str, List]:
    game_df: List = []
    winning_pocket_df: List = []
    inside_bet_df: List = []
    inside_bet_details_df: List = []
    dozen_bet_df: List = []
    column_bet_df: List = []
    odd_or_even_bet_df: List = []
    high_or_low_bet_df: List = []
    color_bet_df: List = []

    game_id = _generate_id()
    winning_pocket_id = _generate_id()

    # Populate game df
    game_df.append(
        {
            "game_id": game_id,
            "winning_pocket_id": winning_pocket_id,
        }
    )

    # Populate winning pocket df
    winning_pocket_df.append(
        {
            "winning_pocket_id": winning_pocket_id,
            **roulette.winning_pocket.to_dict(),
        }
    )

    # populate inside bet and inside bet details dfs
    inside_bets = (
        roulette.bets.straight_up
        + roulette.bets.split
        + roulette.bets.line
        + roulette.bets.five_number_bet
        + roulette.bets.street
    )
    for bet in inside_bets:

        inside_bet_df.append(
            {
                "game_id": game_id,
                **bet.as_dict(),
            }
        )

        if isinstance(bet, SinglePocketBet):
            inside_bet_details_df.append(
                _inside_bet_details(
                    bet_id=bet.id,
                    pocket_number=bet.pocket.pocket_number,
                )
            )
        else:
            for pocket in bet.pockets:
                inside_bet_details_df.append(
                    _inside_bet_details(
                        bet_id=bet.id,
                        pocket_number=pocket.pocket_number,
                    )
                )

    for dozen_bet in roulette.bets.dozen:
        dozen_bet_df.append(
            {
                "game_id": game_id,
                **_outside_bet_dict(dozen_bet, bet_type="dozen"),
            }
        )

    for column_bet in roulette.bets.column:
        column_bet_df.append(
            {
                "game_id": game_id,
                **_outside_bet_dict(column_bet, bet_type="column"),
            }
        )

    for odd_or_even_bet in roulette.bets.odd + roulette.bets.even:
        odd_or_even_bet_df.append(
            {
                "game_id": game_id,
                **_outside_bet_dict(odd_or_even_bet, bet_type="odd_or_even"),
            }
        )
    for high_or_low_bet in roulette.bets.eighteen_number_bet:
        high_or_low_bet_df.append(
            {
                "game_id": game_id,
                **_outside_bet_dict(high_or_low_bet, bet_type="high_or_low"),
            }
        )

    for color_bet in roulette.bets.color:
        color_bet_df.append(
            {
                "game_id": game_id,
                **_outside_bet_dict(color_bet, bet_type="color"),
            }
        )

    return {
        __GAME: game_df,
        __WINNING_POCKET: winning_pocket_df,
        __INSIDE_BET: inside_bet_df,
        __INSIDE_BET_DETAILS: inside_bet_details_df,
        __DOZEN_BET: dozen_bet_df,
        __COLUMN_BET: column_bet_df,
        __ODD_OR_EVEN_BET: odd_or_even_bet_df,
        __HIGH_OR_LOW_BET: high_or_low_bet_df,
        __COLOR_BET: color_bet_df,
    }
