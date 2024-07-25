import pytest
import random
from games.poker.poker_game_logic import Player, generate_poker_hand, create_player_pool, determine_winner, evaluate_hand
from games.poker.sim import simulate_poker, CommunityCard


def test_create_player_pool():
    player_pool = create_player_pool(10)
    assert len(player_pool) == 10
    assert all(isinstance(player, Player) for player in player_pool.values())


def test_deal_hole_cards():
    deck = [f"{rank}{suit}" for rank in '23456789TJQKA' for suit in 'HDCS']
    player = Player(player_id="test", name="Test Player", behavior="Safe Player")
    player.deal_hole_cards(deck)
    assert len(player.hole_cards) == 2
    assert all(card not in deck for card in player.hole_cards)


def test_evaluate_hand():
    hand = ['2H', '3D', '5S', '9C', 'KD']
    best_hand, high_cards = evaluate_hand(hand)
    assert best_hand == 'hc'
    assert high_cards == [13, 9, 5, 3, 2]


def test_determine_winner():
    hand1 = 'toak'
    hand2 = 'tp'
    hand1_high_cards = [8]
    hand2_high_cards = [6, 4]
    hole_cards_p1 = ['8H', '8D']
    hole_cards_p2 = ['6S', '4C']
    assert determine_winner(hand1, hand2, hand1_high_cards, hand2_high_cards, hole_cards_p1, hole_cards_p2) == 'p1'


def test_generate_poker_hand():
    game_data = generate_poker_hand()
    assert len(game_data['players']) == 2
    assert all('playerId' in player for player in game_data['players'])
    assert 'communityCards' in game_data
    assert 'flop' in game_data['communityCards']
    assert len(game_data['communityCards']['flop']) == 3
    assert 'turn' in game_data['communityCards']
    assert 'river' in game_data['communityCards']


def test_simulate_poker_single_game():
    results = simulate_poker(1)
    assert len(results) == 1
    result = results[0]
    assert result.datetime_start < result.datetime_end
    assert result.totalRounds > 0
    assert len(result.players) == 2
    assert all(player.startingChips >= 5000 for player in result.players)
    assert all(isinstance(player.holeCards, list) and len(player.holeCards) == 2 for player in result.players)
    assert isinstance(result.communityCards, dict)
    assert 'flop' in result.communityCards and len(result.communityCards['flop']) == 3
    assert 'turn' in result.communityCards and isinstance(result.communityCards['turn'], CommunityCard)
    assert 'river' in result.communityCards and isinstance(result.communityCards['river'], CommunityCard)


def test_simulate_poker_multiple_games():
    num_games = 2
    results = simulate_poker(num_games)
    assert len(results) == num_games
    for result in results:
        assert result.datetime_start < result.datetime_end
        assert result.totalRounds > 0
        assert len(result.players) == 2
        assert all(player.startingChips >= 5000 for player in result.players)
        assert all(isinstance(player.holeCards, list) and len(player.holeCards) == 2 for player in result.players)
        assert isinstance(result.communityCards, dict)
        assert 'flop' in result.communityCards and len(result.communityCards['flop']) == 3
        assert 'turn' in result.communityCards and isinstance(result.communityCards['turn'], CommunityCard)
        assert 'river' in result.communityCards and isinstance(result.communityCards['river'], CommunityCard)
