from abc import ABC, abstractmethod
from .roulette_bet_type import RouletteBetType


class RouletteBet(ABC):
    id: str = None
    type: RouletteBetType
    bet_amount: float
    amount_won: float = None

    @abstractmethod
    def compute_winnings() -> None:
        raise Exception("Unimplemented Error")
