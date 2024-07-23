import pytest
import random
from games.baccarat.helper_functions import build_deck, rebuild_deck, build_combinations, announce_winner, announce_bet_winner, compute_payout, play_game
from games.baccarat.sim import simulate_baccarat

random.seed = 123542

def test_build_deck():
    deck = build_deck()
    assert len(deck) == 52
    assert len(set(deck)) == 52


def test_rebuild_deck():
    deck_remaining = rebuild_deck(build_deck(), ('5 of Hearts', 'K of Clubs'))
    assert len(deck_remaining) == 50
    assert ('5 of Hearts') not in deck_remaining
    assert ('K of Clubs') not in deck_remaining


def test_build_combinations():
    card_combinations, card_combinations_df, deck_dict = build_combinations(build_deck())
    assert len(card_combinations) == (52 * 51)/2
    assert len(card_combinations_df) == (52 * 51)/2
    assert isinstance(deck_dict, dict)


def test_announce_winner():
    assert announce_winner(player_hand_value=9, banker_hand_value=8) == 'Player'
    assert announce_winner(player_hand_value=5, banker_hand_value=8) == 'Banker'
    assert announce_winner(player_hand_value=0, banker_hand_value=0) == 'Tie'


def test_announce_bet_winner():
    assert announce_bet_winner(player_bet='Player', winner='Tie') == 'Player bet on player losses!'
    assert announce_bet_winner(player_bet='Player', winner='Player') == 'Player bet on player wins!'
    assert announce_bet_winner(player_bet='Banker', winner='Tie') == 'Player bet on banker losses!'
    assert announce_bet_winner(player_bet='Tie', winner='Tie') == 'Player bet on tie wins!'
    assert announce_bet_winner(player_bet='Tie', winner='Player') == 'Player bet on tie losses!'
    assert announce_bet_winner(player_bet='Tie', winner='Banker') == 'Player bet on tie losses!'


def test_compute_payout():
    assert compute_payout(winner='Player', wager=100, bet='Player') == 100
    assert compute_payout(winner='Banker', wager=100, bet='Banker') == 95
    assert compute_payout(winner='Player', wager=100, bet='Banker') == -100
    assert compute_payout(winner='Tie', wager=10.5, bet='Tie') == 84


def test_simulate_baccarat():
    result = simulate_baccarat()
    assert result.start_time < result.end_time
    assert result.player_hand_value == int(str(sum(10 if card['value'] in ['K', 'Q', 'J'] else 1 if card['value'] == 'A' else int(card['value']) for card in result.player_hand))[-1])
    assert result.banker_hand_value == int(str(sum(10 if card['value'] in ['K', 'Q', 'J'] else 1 if card['value'] == 'A' else int(card['value']) for card in result.banker_hand))[-1])
    assert result.player_ending_balance - result.player_payout == result.player_beginning_balance
