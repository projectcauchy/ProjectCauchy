from dataclasses import dataclass
from typing import List


@dataclass
class CardResponse:
    suit: str
    value: str

    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value


@dataclass
class TransactionResponse:
    player_id: str
    timestamp: str
    gameId: str
    status: str
    playerHand: List[CardResponse]
    playerHandValue: int
    dealerHand: List[CardResponse]
    dealerHandValue: int
    currentBet: int
    playerBalance: int
    availableActions: List[str]
    lastAction: str
    outcome: str
    payout: int

    def __init__(
        self,
        playerId: str,
        timestamp: str,
        gameId: str,
        status: str,
        playerHand: List,
        playerHandValue: int,
        dealerHand: List,
        dealerHandValue: int,
        currentBet: int,
        playerBalance: int,
        availableActions: List,
        lastAction: str,
        outcome: str,
        payout: int,
    ) -> None:
        self.player_id = playerId
        self.timestamp = timestamp
        self.gameId = gameId
        self.status = status
        self.playerHand = [CardResponse(**card) for card in playerHand]
        self.playerHandValue = playerHandValue
        self.dealerHand = [CardResponse(**card) for card in dealerHand]
        self.dealerHandValue = dealerHandValue
        self.currentBet = currentBet
        self.playerBalance = playerBalance
        self.availableActions = availableActions
        self.lastAction = lastAction
        self.outcome = outcome
        self.payout = payout


@dataclass
class BlackJackResponse:
    num_players: int
    num_games: int
    transactions: List[TransactionResponse]

    def __init__(self, numPlayers: int, numGames: int, transactions: List) -> None:
        self.num_players = numPlayers
        self.num_games = numGames
        self.transactions = [
            TransactionResponse(**transaction) for transaction in transactions
        ]
