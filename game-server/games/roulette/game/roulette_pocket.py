from enum import Enum


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
