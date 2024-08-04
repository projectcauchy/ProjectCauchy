from enum import Enum
from ..bet import RouletteBetType, Dozen, Column, HighOrLow


class PocketColor(Enum):
    RED: str = "RED"
    BLACK: str = "BLACK"
    GREEN: str = "GREEN"


class RoulettePocket:
    """
    Represents a pocket in a Roulette
    - [pocket_color]: The color of the winning pocket
    - [pocket_number]: The number of the winning pocket, -1 being the double-zero (00) and 0 being zero(0)
    """

    pocket_color: PocketColor
    pocket_number: int

    def __init__(self, pocket_number) -> None:
        self.pocket_number = pocket_number
        self.pocket_color = self._get_pocket_color()

    def _get_pocket_color(self) -> PocketColor:
        if self.pocket_number <= 0:
            return PocketColor.GREEN
        is_even = self.pocket_number % 2 == 0
        if self.pocket_number <= 10:
            return PocketColor.BLACK if is_even else PocketColor.RED
        if self.pocket_number <= 18:
            return PocketColor.RED if is_even else PocketColor.BLACK
        if self.pocket_number <= 28:
            return PocketColor.BLACK if is_even else PocketColor.RED

        return PocketColor.RED if is_even else PocketColor.BLACK

    def __eq__(self, other):
        if not isinstance(other, RoulettePocket):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (
            self.pocket_number == other.pocket_number
            and self.pocket_color == other.pocket_color
        )


class WinningPocket(RoulettePocket):
    """
    Represents wining pocket in a Roulette. Contains outside bet details, that not necessary in a normal pocket
    - [pocket_color]: The color of the winning pocket
    - [pocket_number]: The number of the winning pocket, -1 being the double-zero (00) and 0 being zero(0)
    - [odd_or_even]: Is the pocket number even or odd number
    - [column]: is the pocket located in first, second, or third column
    - [dozen]: is the pocket located in first, second, or third dozen
    - [high_or_low]: is the number located in first or second eighteen
        - first eighteen is LOW
        - second eighteen is HIGH
    """

    pocket_color: PocketColor
    pocket_number: int
    odd_or_even: RouletteBetType
    column: Column = None
    dozen: Dozen = None
    high_or_low: HighOrLow = None

    def __init__(self, pocket_number) -> None:
        self.pocket_number = pocket_number
        self.pocket_color = self._get_pocket_color()
        self._get_odd_or_even()
        self._get_column_pos()
        self._get_dozen_pos()
        self._get_high_or_low()

    def _get_pocket_color(self) -> PocketColor:
        if self.pocket_number <= 0:
            return PocketColor.GREEN
        is_even = self.pocket_number % 2 == 0
        if self.pocket_number <= 10:
            return PocketColor.BLACK if is_even else PocketColor.RED
        if self.pocket_number <= 18:
            return PocketColor.RED if is_even else PocketColor.BLACK
        if self.pocket_number <= 28:
            return PocketColor.BLACK if is_even else PocketColor.RED

        return PocketColor.RED if is_even else PocketColor.BLACK

    def _get_column_pos(self) -> Column:
        if self.pocket_number <= 0:
            return

        if self.pocket_number % 3 == 1:
            self.column = Column.FIRST_COLUMN
        elif self.pocket_number % 3 == 2:
            self.column = Column.SECOND_COLUMN
        else:
            self.column = Column.THIRD_COLUMN

    def _get_dozen_pos(self) -> Column:
        if self.pocket_number <= 0:
            return
        if self.pocket_number <= 12:
            self.dozen = Dozen.FIRST_DOZEN
        elif self.pocket_number <= 24:
            self.dozen = Dozen.SECOND_DOZEN
        else:
            self.dozen = Dozen.THIRD_DOZEN

    def _get_high_or_low(self) -> Column:
        if self.pocket_number <= 0:
            return
        self.high_or_low = HighOrLow.LOW if self.pocket_number <= 18 else HighOrLow.HIGH

    def _get_odd_or_even(self):
        if self.pocket_number < 0:
            self.odd_or_even = RouletteBetType.EVEN
        else:
            self.odd_or_even = (
                RouletteBetType.EVEN
                if self.pocket_number % 2 == 0
                else RouletteBetType.ODD
            )
