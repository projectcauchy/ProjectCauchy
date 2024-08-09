from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class WinningPocketResponse:
    pocket_number: int = None
    pocket_color: str = None
    odd_or_even: Optional[str] = None
    column: Optional[str] = None
    dozen: Optional[str] = None
    high_or_low: Optional[str] = None
