from collections import defaultdict
from dataclasses import dataclass

from typing import Dict, List
from copy import deepcopy

from .bet import random_bet, RouletteBet

from .game import RouletteGame, RoulettePocket


@dataclass
class RouletteResult:
    winning_pocket: RoulettePocket
    winning_bets: Dict
    bets: Dict


def simulate_roulette() -> RouletteResult:
    game = RouletteGame()

    for bet in [random_bet(game) for _ in range(100)]:
        game.add_bet(bet)

    game.spin()

    return RouletteResult(
        winning_pocket=game._winning_pocket,
        winning_bets=game.get_winning_bets(),
        bets=game.get_all_bets(),
    )
