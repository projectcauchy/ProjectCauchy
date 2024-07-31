from collections import defaultdict
from random import Random
from typing import List
from .roulette_pocket import RoulettePocket, PocketColor
from ..bet.roulette_bet import RouletteBet


class RouletteGame:
    _pockets = List[RoulettePocket]
    _winning_pocket: RoulettePocket = None
    _bets: List[RouletteBet] = []

    def __init__(self):
        self._pockets = [RoulettePocket(pocket_number=i) for i in range(-1, 37)]

    def spin(self):
        row = Random().randint(1, 12)
        col = Random().randint(1, 3)
        self._winning_pocket = self.pocket_from_coord(row, col)

        for bet in self._bets:
            bet.compute_winnings(self._winning_pocket)

    def get_winning_bets(self) -> List[RouletteBet]:
        winning_bets = defaultdict(list)

        for bet in self._bets:
            if bet.amount_won != None:
                winning_bets[bet.type].append(bet)

        return dict(winning_bets)

    def get_all_bets(self) -> List[RouletteBet]:
        all_bets = defaultdict(list)

        for bet in self._bets:
            all_bets[bet.type].append(bet)

        return dict(all_bets)

    def clear_bets(self):
        self._bets.clear()

    def add_bet(self, bet: RouletteBet):
        self._bets.append(bet)

    def pocket_from_coord(self, row: int, col: int) -> RoulettePocket:
        pocket_number = col + ((row - 1) * 3)
        for pocket in self._pockets:
            if pocket_number == pocket.pocket_number:
                return pocket

    def pocket_from_pocket_number(self, pocket_number: int) -> RoulettePocket:
        for pocket in self._pockets:
            if pocket_number == pocket.pocket_number:
                return pocket

    def pockets_from_color(self, color: PocketColor) -> List[RoulettePocket]:
        return [pocket for pocket in self._pockets if pocket.pocket_color == color]
