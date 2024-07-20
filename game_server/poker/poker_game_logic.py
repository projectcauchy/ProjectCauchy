import random
import hashlib
import datetime
import json
from .hand_evaluation import evaluate_hand, is_royal_flush, is_straight_flush, is_four_of_a_kind, is_full_house, is_flush, is_straight, is_three_of_a_kind, is_two_pair, is_pair, get_high_cards, get_four_of_a_kind_high_card, get_full_house_high_cards, get_three_of_a_kind_high_card, get_two_pair_high_cards, get_pair_high_cards

win_options = ['All in', 'Showdown', 'Forfeit', 'Fold']
wo_probabilities = [0.10, 0.40, 0.05, 0.45]

winning_hands = ['rf', 'sf', 'foak', 'fh', 'fl', 'st', 'toak', 'tp', 'pa', 'hc']
wh_probabilities = [0.000015, 0.00015, 0.0015, 0.025, 0.03, 0.15, 0.02, 0.23, 0.43, 0.14435]

suits = ['H', 'D', 'C', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
deck_template = [rank + suit for suit in suits for rank in ranks]
rank_values = {rank: index for index, rank in enumerate(ranks, start=2)}

hand_values = {
    'hc': 1,
    'pa': 2,
    'tp': 3,
    'toak': 4,
    'st': 5,
    'fl': 6,
    'fh': 7,
    'foak': 8,
    'sf': 9,
    'rf': 10
}


class Player:
    def __init__(self, player_id, name, behavior):
        self.player_id = player_id
        self.name = name
        self.behavior = behavior
        self.hole_cards = []
        self.folded = False
        self.forfeited = False
        self.bets_made = 0
        self.net_win = 0
        self.chips = random.randint(5000, 40000)

    def deal_hole_cards(self, deck):
        self.hole_cards = random.sample(deck, 2)
        for card in self.hole_cards:
            deck.remove(card)

    def fold(self):
        self.folded = True

    def forfeit(self):
        self.forfeited = True

    def reset(self):
        self.hole_cards = []
        self.folded = False
        self.forfeited = False

    def __str__(self):
        return f"{self.name} ({self.player_id}, {self.behavior}): Hole Cards = {self.hole_cards}"


def generate_player_id(name):
    full_hash = hashlib.sha256(name.encode()).hexdigest()
    return full_hash[:25]


def create_player_pool(num_players):
    player_pool = {}
    behaviors = ['High Gambler', 'Safe Player', 'Low Baller']
    for i in range(num_players):
        name = f"Player {i+1}"
        player_id = generate_player_id(name)
        behavior = random.choice(behaviors)
        player_pool[player_id] = Player(player_id, name, behavior)
    return player_pool


def draw_cards(deck, num):
    return random.sample(deck, num)

def generate_hole_and_community_cards(player_1, player_2):
    deck = deck_template.copy()
    random.shuffle(deck)

    player_1.deal_hole_cards(deck)
    player_2.deal_hole_cards(deck)

    community_cards = draw_cards(deck, 5)
    return player_1.hole_cards, player_2.hole_cards, community_cards


def determine_winner(hand1, hand2, hand1_high_cards, hand2_high_cards, hole_cards_p1, hole_cards_p2):
    if hand_values[hand1] > hand_values[hand2]:
        return "p1"
    elif hand_values[hand1] < hand_values[hand2]:
        return "p2"
    else:
        for h1, h2 in zip(hand1_high_cards, hand2_high_cards):
            if h1 > h2:
                return "p1"
            elif h1 < h2:
                return "p2"

        hole_card_values_p1 = sorted([rank_values[card[:-1]] for card in hole_cards_p1], reverse=True)
        hole_card_values_p2 = sorted([rank_values[card[:-1]] for card in hole_cards_p2], reverse=True)

        for h1, h2 in zip(hole_card_values_p1, hole_card_values_p2):
            if h1 > h2:
                return "p1"
            elif h1 < h2:
                return "p2"

        return "tie"


def generate_winnings(winner, player1, player2, player1_bets, player2_bets):
    rake = 5
    initial_bets = 10
    total_pot = player1_bets + player2_bets + (initial_bets * 2)
    house_earnings = total_pot * (rake / 100)
    player1_netwin = 0
    player2_netwin = 0
    total_chips_dist = total_pot - house_earnings

    if winner == "p1":
        player1_netwin = total_chips_dist - (initial_bets + player1_bets)
        player2_netwin = -1 * (player2_bets + initial_bets)
    elif winner == "p2":
        player2_netwin = total_chips_dist - (initial_bets + player2_bets)
        player1_netwin = -1 * (player1_bets + initial_bets)
    elif winner == "tie":
        player1_netwin, player2_netwin =  (total_chips_dist - player1_bets) / 2

    player1.net_win += player1_netwin
    player2.net_win += player2_netwin

    return player1_netwin, player2_netwin, house_earnings, total_pot, rake, initial_bets


def place_bets(player1, player2, win_option):
    if win_option == 'All in':
        player1_bets = player1.chips
        player2_bets = player2.chips
    else:
        player1_bets = random.randint(5000, min(player1.chips, 40000))
        player2_bets = min(player1_bets, player2.chips)  # Match player1's bet or go all-in if player2 has less chips

    return player1_bets, player2_bets


def generate_employee_id():
    return hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()[:6]


def game_details(rounds):
    game_id = hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()[:24]
    dealer_behaviors = ['Sus', 'Sus', 'Good', 'Good', 'Good', 'Good', 'Good', 'Good']
    dealer_ids = {
        "Dealer01": {"behavior": "Sus", "employeeId": "a1b2c3"},
        "Dealer02": {"behavior": "Sus", "employeeId": "d4e5f6"},
        "Dealer03": {"behavior": "Good", "employeeId": "g7h8i9"},
        "Dealer04": {"behavior": "Good", "employeeId": "j0k1l2"},
        "Dealer05": {"behavior": "Good", "employeeId": "m3n4o5"},
        "Dealer06": {"behavior": "Good", "employeeId": "p6q7r8"},
        "Dealer07": {"behavior": "Good", "employeeId": "s9t0u1"},
        "Dealer08": {"behavior": "Good", "employeeId": "v2w3x4"}
    }
    selected_dealer = random.choice(list(dealer_ids.keys()))
    selected_dealer_behavior = dealer_ids[selected_dealer]['behavior']
    selected_dealer_employee_id = dealer_ids[selected_dealer]['employeeId']
    datetime_start = datetime.datetime.now().replace(microsecond=0)
    datetime_end = (datetime_start + datetime.timedelta(minutes=random.randint(5, 10) * rounds)).replace(microsecond=0)

    return {
        "game_id": game_id,
        "dealer_ids": dealer_ids,
        "selected_dealer": selected_dealer,
        "selected_dealer_behavior": selected_dealer_behavior,
        "selected_dealer_employee_id": selected_dealer_employee_id,
        "datetime_start": datetime_start,
        "datetime_end": datetime_end
    }


def generate_poker_hand():
    player_pool = create_player_pool(100)
    player_ids = random.sample(list(player_pool.keys()), 2)
    player_1 = player_pool[player_ids[0]]
    player_2 = player_pool[player_ids[1]]

    hole_cards_p1, hole_cards_p2, community_cards = generate_hole_and_community_cards(player_1, player_2)

    best_hand_p1, high_cards_p1 = evaluate_hand(hole_cards_p1 + community_cards)
    best_hand_p2, high_cards_p2 = evaluate_hand(hole_cards_p2 + community_cards)

    win_option = random.choices(win_options, wo_probabilities)[0]

    if win_option == 'Showdown':
        rounds = 4
    else:
        rounds = random.randint(1, 4)

    player1_bets, player2_bets = place_bets(player_1, player_2, win_option)

    if win_option in ['All in', 'Showdown']:
        winner = determine_winner(best_hand_p1, best_hand_p2, high_cards_p1, high_cards_p2, hole_cards_p1, hole_cards_p2)
    elif win_option == 'Forfeit':
        player_1.forfeit()
        winner = "p2"
    elif win_option == 'Fold':
        player_1.fold()
        winner = "p2"

    player1_netwin, player2_netwin, house_earnings, total_pot, rake, initial_bets = generate_winnings(winner, player_1, player_2, player1_bets, player2_bets)

    game_info = game_details(rounds)

    game_data = {
        "gameID": game_info['game_id'],
        "datetime_start": game_info['datetime_start'].strftime("%Y-%m-%d %H:%M:%S"),
        "datetime_end": game_info['datetime_end'].strftime("%Y-%m-%d %H:%M:%S"),
        "employeeDealerId": game_info['selected_dealer_employee_id'],
        "totalRounds": rounds,
        "winType": win_option.lower(),
        "winner": player_1.player_id if winner == "p1" else player_2.player_id,
        "totalPot": total_pot,
        "initialBlind": initial_bets,
        "rake": rake,
        "players": [
            {
                "playerId": player_1.player_id,
                "holeCards": [{"rank": rank_values[card[:-1]], "suit": card[-1]} for card in player_1.hole_cards],
                "startingChips": player_1.chips,
                "bestHand": best_hand_p1,
                "netWin": player1_netwin
            },
            {
                "playerId": player_2.player_id,
                "holeCards": [{"rank": rank_values[card[:-1]], "suit": card[-1]} for card in player_2.hole_cards],
                "startingChips": player_2.chips,
                "bestHand": best_hand_p2,
                "netWin": player2_netwin
            }
        ],
        "communityCards": {
            "flop": [{"rank": rank_values[card[:-1]], "suit": card[-1]} for card in community_cards[:3]],
            "turn": {"rank": rank_values[community_cards[3][:-1]], "suit": community_cards[3][-1]},
            "river": {"rank": rank_values[community_cards[4][:-1]], "suit": community_cards[4][-1]}
        }
    }

    return game_data
