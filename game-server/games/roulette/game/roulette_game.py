from collections import defaultdict
from random import Random
from typing import List
from .roulette_pocket import RoulettePocket, PocketColor
from ..bet.roulette_bet import RouletteBet


class RouletteGame:
    __pockets = List[RoulettePocket]
    __winning_pocket: RoulettePocket = None
    __bets: List[RouletteBet] = []

    def __init__(self):
        self.__pockets = [RoulettePocket(pocket_number=i) for i in range(-1, 37)]

    def spin(self):
        row = Random().randint(1, 12)
        col = Random().randint(1, 3)
        self.__winning_pocket = self.pocket_from_coord(row, col)

        for bet in self.__bets:
            bet.compute_winnings(self.__winning_pocket)

    def get_winning_pocket(self) -> RoulettePocket:
        return self.__winning_pocket

    def get_winning_bets(self) -> List[RouletteBet]:
        winning_bets = defaultdict(list)

        for bet in self.__bets:
            if bet.amount_won != None:
                winning_bets[bet.type].append(bet)

        return dict(winning_bets)

    def get_all_bets(self) -> List[RouletteBet]:
        all_bets = defaultdict(list)

        for bet in self.__bets:
            all_bets[bet.type].append(bet)

        return dict(all_bets)

    def clear_bets(self):
        self.__bets.clear()

    def add_bet(self, bet: RouletteBet):
        self.__bets.append(bet)

    def pocket_from_coord(self, row: int, col: int) -> RoulettePocket:
        pocket_number = col + ((row - 1) * 3)
        for pocket in self.__pockets:
            if pocket_number == pocket.pocket_number:
                return pocket

    def pocket_from_pocket_number(self, pocket_number: int) -> RoulettePocket:
        for pocket in self.__pockets:
            if pocket_number == pocket.pocket_number:
                return pocket

    def pockets_from_color(self, color: PocketColor) -> List[RoulettePocket]:
        return [pocket for pocket in self.__pockets if pocket.pocket_color == color]
