from dataclasses import dataclass, field
from dataclasses_json import config, dataclass_json
from typing import Dict, List, Optional


@dataclass_json
@dataclass
class Pocket:
    pocket_number: Optional[int] = None
    pocket_color: Optional[str] = None


@dataclass_json
@dataclass
class SinglePocketBet:
    id: Optional[str] = None
    type: Optional[str] = None
    bet_amount: Optional[float] = None
    amount_won: Optional[float] = None
    pocket: Optional[Pocket] = None

    def as_dict(self) -> Dict[str, any]:
        return {
            "inside_bet_id": self.id,
            "type": self.type,
            "bet_amount": self.bet_amount,
            "amount_won": self.amount_won,
        }


@dataclass_json
@dataclass
class MultiPocketBet:
    id: Optional[str] = None
    type: Optional[str] = None
    bet_amount: Optional[float] = None
    amount_won: Optional[float] = None
    pockets: List[Pocket] = field(default_factory=lambda: [])

    def as_dict(self) -> Dict[str, any]:
        return {
            "inside_bet_id": self.id,
            "type": self.type,
            "bet_amount": self.bet_amount,
            "amount_won": self.amount_won,
        }


@dataclass_json
@dataclass
class OutsideBet:
    id: Optional[str] = None
    type: Optional[str] = None
    bet_amount: Optional[float] = None
    amount_won: Optional[float] = None
    bet: Optional[str] = None


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
