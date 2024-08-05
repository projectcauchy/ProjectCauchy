from enum import Enum


class RouletteBetType(Enum):
    STRAIGHT_UP: str = "STRAIGHT_UP"
    SPLIT: str = "SPLIT"
    STREET: str = "STREET"
    FIVE_NUMBER_BET: str = "FIVE_NUMBER_BET"
    LINE: str = "LINE"
    DOZEN: str = "DOZEN"
    COLUMN: str = "COLUMN"
    EIGHTEEN_NUMBER_BET: str = "EIGHTEEN_NUMBER_BET"
    COLOR: str = "COLOR"
    ODD: str = "ODD"
    EVEN: str = "EVEN"


class Dozen(Enum):
    FIRST_DOZEN: str = "FIRST_DOZEN"
    SECOND_DOZEN: str = "SECOND_DOZEN"
    THIRD_DOZEN: str = "THIRD_DOZEN"


class HighOrLow(Enum):
    LOW: str = "LOW"
    HIGH: str = "HIGH"


class Column(Enum):
    FIRST_COLUMN: str = "FIRST_COLUMN"
    SECOND_COLUMN: str = "SECOND_COLUMN"
    THIRD_COLUMN: str = "THIRD_COLUMN"
