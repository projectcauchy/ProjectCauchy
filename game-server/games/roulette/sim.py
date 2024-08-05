from collections import defaultdict
from dataclasses import dataclass

from typing import Dict, List

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
        winning_pocket=game.get_winning_pocket(),
        winning_bets=_bets_as_dict(game.get_winning_bets()),
        bets=_bets_as_dict(game.get_all_bets()),
    )


def _bets_as_dict(bet_list: List[RouletteBet]) -> Dict:
    bets = defaultdict(list)
    for bet in bet_list:
        bets[bet.type].append(bet)

    return dict(bets)
