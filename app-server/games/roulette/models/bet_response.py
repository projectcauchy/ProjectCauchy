from dataclasses import dataclass, field
from dataclasses_json import LetterCase, config, dataclass_json
from typing import Any, List, Optional


@dataclass_json
@dataclass
class Pocket:
    pocket_number: int = None
    pocket_color: str = None


@dataclass_json
@dataclass
class SinglePocketBet:
    id: str = None
    type: str = None
    bet_amount: float = None
    amount_won: float = None
    pocket: Pocket = None


@dataclass_json
@dataclass
class MultiPocketBet:
    id: str = None
    type: str = None
    bet_amount: float = None
    amount_won: float = None
    pockets: List[Pocket] = None


@dataclass_json
@dataclass
class OutsideBet:
    id: str = None
    type: str = None
    bet_amount: float = None
    amount_won: float = None
    bet: str = None


@dataclass_json
@dataclass
class BetResponse:
    straight_up: Optional[List[SinglePocketBet]] = field(
        metadata=config(field_name="STRAIGHT_UP"),
        default=None,
    )
    split: Optional[List[MultiPocketBet]] = field(
        metadata=config(field_name="SPLIT"),
        default=None,
    )
    line: Optional[List[MultiPocketBet]] = field(
        metadata=config(field_name="LINE"),
        default=None,
    )
    five_number_bet: Optional[List[MultiPocketBet]] = field(
        metadata=config(field_name="FIVE_NUMBER_BET"),
        default=None,
    )
    street: Optional[List[MultiPocketBet]] = field(
        metadata=config(field_name="STREET"),
        default=None,
    )
    dozen: Optional[List[OutsideBet]] = field(
        metadata=config(field_name="DOZEN"),
        default=None,
    )
    column: Optional[List[OutsideBet]] = field(
        metadata=config(field_name="COLUMN"),
        default=None,
    )
    eighteen_number_bet: Optional[List[OutsideBet]] = field(
        metadata=config(field_name="EIGHTEEN_NUMBER_BET"),
        default=None,
    )
    color: Optional[List[OutsideBet]] = field(
        metadata=config(field_name="COLOR"),
        default=None,
    )
    odd: Optional[List[OutsideBet]] = field(
        metadata=config(field_name="ODD"),
        default=None,
    )
    even: Optional[List[OutsideBet]] = field(
        metadata=config(field_name="EVEN"),
        default=None,
    )
