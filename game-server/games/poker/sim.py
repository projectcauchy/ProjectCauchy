from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class PokerResult:
    starttime: datetime
    endtime: datetime
    betamount: float

def simulate_poker() -> PokerResult:
    return PokerResult(datetime.now(), datetime.now() + timedelta(hours=2), 20)
