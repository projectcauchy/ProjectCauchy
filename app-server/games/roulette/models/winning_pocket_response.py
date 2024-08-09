from dataclasses import dataclass

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class WinningPocketResponse:
    pocket_number: int = None
    pocket_color: str = None
    odd_or_even: str = None
    column: str = None
    dozen: str = None
    high_or_low: str = None
