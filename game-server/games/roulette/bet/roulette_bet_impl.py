from dataclasses import dataclass
from random import Random
import string
from typing import List
from .roulette_bet_type import (
    ColumnBetType,
    DozenBetType,
    EighteenNumberBetType,
    RouletteBetType,
)
from .roulette_bet import RouletteBet
from ..game.roulette_pocket import PocketColor, RoulettePocket


def _generate_id() -> str:
    return "RBID-" + "".join(
        Random().choices(
            string.ascii_uppercase + string.digits,
            k=6,
        )
    )


@dataclass
class StraightUpBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.STRAIGHT_UP
    bet_amount: float = None
    amount_won: float = None
    pocket: RoulettePocket = None

    def __init__(
        self,
        bet_amount: float,
        pocket: RoulettePocket,
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pocket = pocket

    def compute_winnings(self, winning_pocket: RoulettePocket):
        if winning_pocket == self.pocket:
            self.amount_won = self.bet_amount * 35


@dataclass
class SplitBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.SPLIT
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self, winning_pocket: RoulettePocket):
        if winning_pocket in self.pockets:
            self.amount_won = self.bet_amount * 17


@dataclass
class StreetBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.STREET
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self, winning_pocket: RoulettePocket):
        if winning_pocket in self.pockets:
            self.amount_won = self.bet_amount * 11


@dataclass
class FiveNumberBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.FIVE_NUMBER_BET
    bet_amount: float = None
    amount_won: float = None

    def __init__(
        self,
        bet_amount: float,
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount

    def compute_winnings(self, winning_pocket: RoulettePocket):
        if winning_pocket.pocket_number <= 3:
            self.amount_won = self.bet_amount * 11


@dataclass
class LineBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.LINE
    bet_amount: float = None
    amount_won: float = None
    pockets: List[RoulettePocket] = None

    def __init__(
        self,
        bet_amount: float,
        pockets: List[RoulettePocket],
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.pockets = pockets

    def compute_winnings(self, winning_pocket: RoulettePocket):
        if winning_pocket in self.pockets:
            self.amount_won = self.bet_amount * 5


@dataclass
class DozenBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.DOZEN
    bet_amount: float = None
    amount_won: float = None
    bet: DozenBetType = None

    def __init__(
        self,
        bet_amount: float,
        bet: DozenBetType,
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.bet = bet

    def compute_winnings(self, winning_pocket: RoulettePocket):
        if winning_pocket.pocket_number <= 0:
            return
        winning_bet: DozenBetType
        if winning_pocket.pocket_number <= 12:
            winning_bet = DozenBetType.FIRST_DOZEN
        elif winning_pocket.pocket_number <= 24:
            winning_bet = DozenBetType.SECOND_DOZEN
        else:
            winning_bet = DozenBetType.THIRD_DOZEN

        if winning_bet == self.bet:
            self.amount_won = self.bet_amount * 2


@dataclass
class ColumnBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.COLUMN
    bet_amount: float = None
    amount_won: float = None
    bet: ColumnBetType = None

    def __init__(
        self,
        bet_amount: float,
        bet: ColumnBetType,
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.bet = bet

    def compute_winnings(self, winning_pocket: RoulettePocket):
        if winning_pocket.pocket_number <= 0:
            return
        winning_bet: ColumnBetType
        if winning_pocket.pocket_number % 3 == 1:
            winning_bet = ColumnBetType.FIRST_COLUMN
        elif winning_pocket.pocket_number % 3 == 2:
            winning_bet = ColumnBetType.SECOND_COLUMN
        else:
            winning_bet = ColumnBetType.THIRD_COLUMN

        if winning_bet == self.bet:
            self.amount_won = self.bet_amount * 2


@dataclass
class EighteenNumberBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.EIGHTEEN_NUMBER_BET
    bet_amount: float = None
    amount_won: float = None
    bet: EighteenNumberBetType = None

    def __init__(
        self,
        bet_amount: float,
        bet: EighteenNumberBetType,
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.bet = bet

    def compute_winnings(self, winning_pocket: RoulettePocket):
        if winning_pocket.pocket_number <= 0:
            return
        winning_bet: EighteenNumberBetType = (
            EighteenNumberBetType.FIRST_EIGHTEEN
            if winning_pocket.pocket_number <= 18
            else EighteenNumberBetType.SECOND_EIGHTEEN
        )
        if self.bet == winning_bet:
            self.amount_won = self.bet_amount


@dataclass
class ColorBet(RouletteBet):
    id: str = None
    type: RouletteBetType = RouletteBetType.COLOR
    bet_amount: float = None
    amount_won: float = None
    bet: PocketColor = None

    def __init__(
        self,
        bet_amount: float,
        bet: PocketColor,
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.bet = bet

    def compute_winnings(self, winning_pocket: RoulettePocket):
        if winning_pocket.pocket_color == self.bet:
            self.amount_won = self.bet_amount


@dataclass
class OddOrEvenBet(RouletteBet):
    id: str = None
    type: RouletteBetType = None
    bet_amount: float = None
    amount_won: float = None

    def __init__(
        self,
        bet_amount: float,
        bet: RouletteBetType,
    ) -> None:
        self.id = _generate_id()
        self.bet_amount = bet_amount
        self.type = bet

    def compute_winnings(self, winning_pocket: RoulettePocket):
        remainder = 1 if self.type == RouletteBetType.ODD else 0
        winning_pocket_number = (
            0 if winning_pocket.pocket_number < 0 else winning_pocket.pocket_number
        )
        if winning_pocket_number % 2 == remainder:
            self.amount_won = self.bet_amount
