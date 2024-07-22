import sys
import os
import string
import random
import datetime
from dataclasses import dataclass

# Adjust the Python path to include the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from helper_functions import play_game, announce_winner, compute_payout

@dataclass
class BaccaratResult:
    game: str
    game_id: str
    player_id: str
    status: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    player_hand: list
    player_hand_value: int
    banker_hand: list
    banker_hand_value: int
    player_beginning_balance: float
    player_wager: float
    player_bet: str
    player_payout: float
    player_ending_balance: float
    last_action: str
    game_outcome: str

def simulate_baccarat() -> BaccaratResult:
    game = "Baccarat"
    game_id = 'GID-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    player_id = 'PID-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    player_beginning_balance = float(random.randint(0, 1001))
    player_wager = float(random.randint(0, int(player_beginning_balance)))  # Wager should be based on beginning balance
    player_bet = random.choice(['Player', 'Banker', 'Tie'])
    status = "Success"
    start_time = datetime.datetime.fromtimestamp(
        random.randint(int(datetime.datetime(2023, 1, 1).timestamp()), 
                       int(datetime.datetime(2024, 6, 30, 23, 59, 59).timestamp())))
    end_time = start_time + datetime.timedelta(minutes=random.randint(1, 3))

    if player_wager > 100:
        game_result = play_game('rigged')
    else:
        game_result = play_game('normal')

    player_hand = [
        {
            'value': game_result.player_hand[0].split(' of ')[1],
            'rank': game_result.player_hand[0].split(' of ')[0]
        },
        {
            'value': game_result.player_hand[1].split(' of ')[1],
            'rank': game_result.player_hand[1].split(' of ')[0]
        },
    ]

    if len(game_result.player_hand) == 3:
        player_hand.append(
            {
                'value': game_result.player_hand[2].split(' of ')[1],
                'rank': game_result.player_hand[2].split(' of ')[0]
            }
        )

    player_hand_value = game_result.player_hand_value

    banker_hand = [
        {
            'value': game_result.banker_hand[0].split(' of ')[1],
            'rank': game_result.banker_hand[0].split(' of ')[0]
        },
        {
            'value': game_result.banker_hand[1].split(' of ')[1],
            'rank': game_result.banker_hand[1].split(' of ')[0]
        },
    ]

    if len(game_result.banker_hand) == 3:
        banker_hand.append(
            {
                'value': game_result.banker_hand[2].split(' of ')[1],
                'rank': game_result.banker_hand[2].split(' of ')[0]
            }
        )

    banker_hand_value = game_result.banker_hand_value

    winner = announce_winner(player_hand_value, banker_hand_value)
    player_payout = compute_payout(winner, player_wager, player_bet)
    player_ending_balance = float(player_beginning_balance + player_payout - player_wager)
    last_action = game_result.last_action
    game_outcome = f'{winner} wins!' if winner in ['Player', 'Banker'] else "It's a tie!"

    return BaccaratResult(
        game, game_id, player_id, status, start_time, end_time,
        player_hand, player_hand_value, banker_hand, banker_hand_value,
        player_beginning_balance, player_wager, player_bet, player_payout, player_ending_balance,
        last_action, game_outcome
    )

# Example usage
result= simulate_baccarat()
print(result)


