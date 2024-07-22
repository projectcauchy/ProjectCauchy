import pytest
from games.blackjack.sim import Card, Deck, calculate_hand_value, simulate_blackjack, simulate_blackjack_games
from datetime import datetime

def test_card_creation():
    card = Card('hearts', 'A')
    assert card.suit == 'hearts'
    assert card.value == 'A'

def test_card_to_dict():
    card = Card('spades', 'K')
    card_dict = card.to_dict()
    assert card_dict == {'suit': 'spades', 'value': 'K'}

def test_deck_creation():
    deck = Deck()
    assert len(deck.cards) == 52

def test_deck_draw():
    deck = Deck()
    card = deck.draw()
    assert isinstance(card, Card)
    assert len(deck.cards) == 51

def test_calculate_hand_value():
    hand = [Card('hearts', 'A'), Card('spades', 'K')]
    assert calculate_hand_value(hand) == 21

    hand = [Card('hearts', '5'), Card('spades', '7'), Card('diamonds', 'K')]
    assert calculate_hand_value(hand) == 22

def test_simulate_blackjack():
    result = simulate_blackjack(1000, 50, datetime.now())
    assert 'gameId' in result
    assert 'playerHand' in result
    assert 'dealerHand' in result
    assert 'outcome' in result

def test_simulate_blackjack_games():
    result = simulate_blackjack_games(2, 3)
    assert result.numPlayers == 2
    assert result.numGames == 3
    assert len(result.transactions) == 6  # 2 players * 3 games


