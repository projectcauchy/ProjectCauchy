from dataclasses import dataclass
from typing import List
from dataclasses_json import dataclass_json

from . import WinningPocketResponse, BetResponse


@dataclass_json
@dataclass
class RouletteResponse:
    winning_pocket: WinningPocketResponse = None
    winning_bets: BetResponse = None
    bets: BetResponse = None
