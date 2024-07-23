from dataclasses import dataclass, field
from typing import List, Dict, Any, Literal
import random
import uuid
from datetime import datetime, timedelta

@dataclass
class BlackjackSimulation:
    numPlayers: int
    numGames: int
    transactions: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class Card:
    suit: Literal['hearts', 'diamonds', 'clubs', 'spades']
    value: Literal['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def to_dict(self) -> Dict[str, str]:
        return {"suit": self.suit, "value": self.value}


class Deck:
    def __init__(self):
        suits: List[Literal['hearts', 'diamonds', 'clubs', 'spades']] = ['hearts', 'diamonds', 'clubs', 'spades']
        values: List[Literal['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']] = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards: List[Card] = [Card(suit, value) for suit in suits for value in values]
        random.shuffle(self.cards)

    def draw(self) -> Card:
        return self.cards.pop()


def calculate_hand_value(hand: List[Card]) -> int:
    value = 0
    aces = 0
    for card in hand:
        if card.value in ['J', 'Q', 'K']:
            value += 10
        elif card.value == 'A':
            aces += 1
        else:
            value += int(card.value)
    
    for _ in range(aces):
        if value + 11 <= 21:
            value += 11
        else:
            value += 1
    
    return value

@dataclass
class BlackjackSimulation:
    numPlayers: int
    numGames: int
    transactions: List[Dict[str, Any]] = field(default_factory=list)


def simulate_blackjack(player_balance: int, bet_amount: int, timestamp: datetime) -> Dict[str, Any]:
    game_id = str(uuid.uuid4())
    deck = Deck()
    player_hand: List[Card] = [deck.draw(), deck.draw()]
    dealer_hand: List[Card] = [deck.draw(), deck.draw()]
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    status = "in_progress"
    available_actions = ["hit", "stand", "double_down"]
    last_action = "initial_deal"
    outcome = None
    payout = 0
    
    # Simulate player's turn
    while player_value < 17:  # Simple strategy: hit on 16 or less
        player_hand.append(deck.draw())
        player_value = calculate_hand_value(player_hand)
        last_action = "hit"
        if player_value > 21:
            status = "completed"
            outcome = "Player busts! Dealer wins."
            payout = -bet_amount
            player_balance += payout
            break

    # Simulate dealer's turn if player hasn't busted
    if status != "completed":
        while dealer_value < 17:
            dealer_hand.append(deck.draw())
            dealer_value = calculate_hand_value(dealer_hand)
        
        status = "completed"
        if dealer_value > 21:
            outcome = "Dealer busts! Player wins."
            payout = bet_amount
        elif dealer_value > player_value:
            outcome = "Dealer wins!"
            payout = -bet_amount
        elif player_value > dealer_value:
            outcome = "Player wins!"
            payout = bet_amount
        else:
            outcome = "It's a tie!"
            payout = 0
        
        player_balance += payout

    return {
        "timestamp": timestamp.isoformat(),
        "gameId": game_id,
        "status": status,
        "playerHand": [card.to_dict() for card in player_hand],
        "playerHandValue": player_value,
        "dealerHand": [dealer_hand[0].to_dict(), {"suit": "hidden", "value": "hidden"}] if status == "in_progress" else [card.to_dict() for card in dealer_hand],
        "dealerHandValue": calculate_hand_value([dealer_hand[0]]) if status == "in_progress" else dealer_value,
        "currentBet": bet_amount,
        "playerBalance": player_balance,
        "availableActions": available_actions if status == "in_progress" else [],
        "lastAction": last_action,
        "outcome": outcome,
        "payout": payout
    }


def simulate_blackjack_games(num_players: int, num_games: int) -> BlackjackSimulation:
    results = []
    start_time = datetime.now()
    for player_id in range(2000, 2000 + num_players):
        player_balance = 1000  # Starting balance for each player
        for game_number in range(num_games):
            bet_amount = random.randint(10, 100)
            # Generate a timestamp for each game
            game_timestamp = start_time + timedelta(seconds=random.randint(0, num_players * num_games * 10))
            game_result = simulate_blackjack(player_balance, bet_amount, game_timestamp)
            player_balance = game_result["playerBalance"]
            
            results.append({
                "playerId": player_id,
                **game_result
            })
    
    # Shuffle the results to randomize the sequence
    random.shuffle(results)
    
    # Sort the results by timestamp after shuffling
    results.sort(key=lambda x: x['timestamp'])
    
    return BlackjackSimulation(numPlayers=num_players, numGames=num_games, transactions=results)