from dataclasses import dataclass, field
import random

@dataclass
class BigWheelResult:
    game: str
    hand_number: int
    result: str
    amount_won: float
    hand_details: dict

def simulate_bigwheel() -> BigWheelResult:
    game = "Big Wheel"
    hand_number = random.randint(10000, 99999)
    result = random.choice(["Win", "Loss"])
    amount_won = round(random.uniform(0, 1000), 2)
    hand_details = {
        "selected_bet": random.choice(["Odd", "Even"]),
        "winning_option": random.choice(["Odd", "Even"]),
        "multiplier": round(random.uniform(1, 5), 1),
        "final_wheel_position": random.randint(1, 20)
    }

    return BigWheelResult(game, hand_number, result, amount_won, hand_details)
