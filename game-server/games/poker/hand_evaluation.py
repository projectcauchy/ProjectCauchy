# card_evaluation.py
from typing import List, Tuple

suits = ['H', 'D', 'C', 'S']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
deck_template = [rank + suit for suit in suits for rank in ranks]
rank_values = {rank: index for index, rank in enumerate(ranks, start=2)}


def evaluate_hand(cards: List[str]) -> Tuple[str, List[int]]:
    if is_royal_flush(cards):
        return 'rf', get_high_cards(cards)
    elif is_straight_flush(cards):
        return 'sf', get_high_cards(cards)
    elif is_four_of_a_kind(cards):
        return 'foak', get_four_of_a_kind_high_card(cards)
    elif is_full_house(cards):
        return 'fh', get_full_house_high_cards(cards)
    elif is_flush(cards):
        return 'fl', get_high_cards(cards)
    elif is_straight(cards):
        return 'st', get_high_cards(cards)
    elif is_three_of_a_kind(cards):
        return 'toak', get_three_of_a_kind_high_card(cards)
    elif is_two_pair(cards):
        return 'tp', get_two_pair_high_cards(cards)
    elif is_pair(cards):
        return 'pa', get_pair_high_cards(cards)
    else:
        return 'hc', get_high_cards(cards)


def is_royal_flush(cards: List[str]) -> bool:
    suits_in_hand = {suit: [] for suit in suits}
    for card in cards:
        rank, suit = card[:-1], card[-1]
        suits_in_hand[suit].append(rank)
    for suit, ranks in suits_in_hand.items():
        if set(ranks) >= {'T', 'J', 'Q', 'K', 'A'}:
            return True
    return False


def is_straight_flush(cards: List[str]) -> bool:
    return is_flush(cards) and is_straight(cards)


def is_four_of_a_kind(cards: List[str]) -> bool:
    ranks_in_hand = [card[:-1] for card in cards]
    for rank in ranks:
        if ranks_in_hand.count(rank) == 4:
            return True
    return False


def is_full_house(cards: List[str]) -> bool:
    ranks_in_hand = [card[:-1] for card in cards]
    three_of_a_kind = None
    pair = None
    for rank in ranks:
        if ranks_in_hand.count(rank) == 3:
            three_of_a_kind = rank
        elif ranks_in_hand.count(rank) == 2:
            pair = rank
    return three_of_a_kind is not None and pair is not None


def is_flush(cards: List[str]) -> bool:
    suits_in_hand = [card[-1] for card in cards]
    for suit in suits:
        if suits_in_hand.count(suit) >= 5:
            return True
    return False


def is_straight(cards: List[str]) -> bool:
    ranks_in_hand = sorted(set([rank_values[card[:-1]] for card in cards]))
    for i in range(len(ranks_in_hand) - 4):
        if ranks_in_hand[i:i + 5] == list(range(ranks_in_hand[i], ranks_in_hand[i] + 5)):
            return True
    if set([2, 3, 4, 5, 14]).issubset(ranks_in_hand):
        return True
    return False


def is_three_of_a_kind(cards: List[str]) -> bool:
    ranks_in_hand = [card[:-1] for card in cards]
    for rank in ranks:
        if ranks_in_hand.count(rank) == 3:
            return True
    return False


def is_two_pair(cards: List[str]) -> bool:
    ranks_in_hand = [card[:-1] for card in cards]
    pairs = 0
    for rank in ranks:
        if ranks_in_hand.count(rank) == 2:
            pairs += 1
    return pairs >= 2


def is_pair(cards: List[str]) -> bool:
    ranks_in_hand = [card[:-1] for card in cards]
    for rank in ranks:
        if ranks_in_hand.count(rank) == 2:
            return True
    return False


def get_high_cards(cards: List[str]) -> List[int]:
    return sorted([rank_values[card[:-1]] for card in cards], reverse=True)


def get_four_of_a_kind_high_card(cards: List[str]) -> List[int]:
    ranks_in_hand = [card[:-1] for card in cards]
    four_of_a_kind = None
    kickers = []
    for rank in ranks:
        if ranks_in_hand.count(rank) == 4:
            four_of_a_kind = rank_values[rank]
        else:
            kickers.append(rank_values[rank])
    kickers.sort(reverse=True)
    return [four_of_a_kind] + kickers[:1]


def get_full_house_high_cards(cards: List[str]) -> List[int]:
    ranks_in_hand = [card[:-1] for card in cards]
    three_of_a_kind = None
    pair = None
    for rank in ranks:
        if ranks_in_hand.count(rank) == 3:
            three_of_a_kind = rank_values[rank]
        elif ranks_in_hand.count(rank) == 2:
            pair = rank_values[rank]
    return [three_of_a_kind, pair]


def get_three_of_a_kind_high_card(cards: List[str]) -> List[int]:
    ranks_in_hand = [card[:-1] for card in cards]
    three_of_a_kind = None
    kickers = []
    for rank in ranks:
        if ranks_in_hand.count(rank) == 3:
            three_of_a_kind = rank_values[rank]
        else:
            kickers.append(rank_values[rank])
    kickers.sort(reverse=True)
    return [three_of_a_kind] + kickers[:2]


def get_two_pair_high_cards(cards: List[str]) -> List[int]:
    ranks_in_hand = [card[:-1] for card in cards]
    pairs = []
    kickers = []
    for rank in ranks:
        if ranks_in_hand.count(rank) == 2:
            pairs.append(rank_values[rank])
        else:
            kickers.append(rank_values[rank])
    pairs.sort(reverse=True)
    kickers.sort(reverse=True)
    return pairs + kickers[:1]


def get_pair_high_cards(cards: List[str]) -> List[int]:
    ranks_in_hand = [card[:-1] for card in cards]
    pair = None
    kickers = []
    for rank in ranks:
        if ranks_in_hand.count(rank) == 2 and pair is None:
            pair = rank_values[rank]
        else:
            kickers.append(rank_values[rank])
    kickers.sort(reverse=True)
    return [pair] + kickers[:3]
