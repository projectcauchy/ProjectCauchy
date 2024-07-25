from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Union


@dataclass
class PlayerResult:
    playerId: str
    holeCards: List[Dict[str, str]]
    startingChips: int
    bestHand: str
    netWin: float


@dataclass
class CommunityCard:
    rank: str
    suit: str


@dataclass
class PokerResult:
    gameID: str
    datetime_start: str
    datetime_end: str
    employeeDealerId: str
    totalRounds: int
    winType: str
    winner: str
    totalPot: float
    initialBlind: float
    rake: float
    players: List[PlayerResult]
    communityCards: Dict[str, Union[List[CommunityCard], CommunityCard]]


def simulate_poker(num_games: int = 1) -> List[PokerResult]:
    from .poker_game_logic import generate_poker_hand
    results = []
    for _ in range(num_games):
        game_data = generate_poker_hand()
        start_time = datetime.now()
        end_time = game_data["datetime_end"]

        # Convert player data
        players = [
            PlayerResult(
                playerId=player["playerId"],
                holeCards=[{"rank": card[:-1], "suit": card[-1]} for card in player["holeCards"]],
                startingChips=player["startingChips"],
                bestHand=player["bestHand"],
                netWin=player["netWin"]
            )
            for player in game_data["players"]
        ]

        # Convert community card data
        community_cards = {
            "flop": [CommunityCard(rank=card["rank"], suit=card["suit"]) for card in game_data["communityCards"]["flop"]],
            "turn": CommunityCard(rank=game_data["communityCards"]["turn"]["rank"], suit=game_data["communityCards"]["turn"]["suit"]),
            "river": CommunityCard(rank=game_data["communityCards"]["river"]["rank"], suit=game_data["communityCards"]["river"]["suit"]),
        }

        result = PokerResult(
            gameID=game_data["gameID"],
            datetime_start=start_time.strftime("%Y-%m-%d %H:%M:%S"),
            datetime_end=end_time,
            employeeDealerId=game_data["employeeDealerId"],
            totalRounds=game_data["totalRounds"],
            winType=game_data["winType"],
            winner=game_data["winner"],
            totalPot=game_data["totalPot"],
            initialBlind=game_data["initialBlind"],
            rake=game_data["rake"],
            players=players,
            communityCards=community_cards
        )

        results.append(result)
    return results
