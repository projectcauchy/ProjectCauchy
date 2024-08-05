from random import randint
from unittest.mock import patch
import pytest
from games.roulette.game import RouletteGame, RoulettePocket, PocketColor
from games.roulette.bet import (
    RouletteBet,
    StraightUpBet,
    SplitBet,
    StreetBet,
    FiveNumberBet,
    LineBet,
    DozenBet,
    ColumnBet,
    EighteenNumberBet,
    ColorBet,
    OddOrEvenBet,
    Dozen,
    Column,
    HighOrLow,
    RouletteBetType,
)


@pytest.fixture
def game():
    return RouletteGame()


def test_initialization(game: RouletteGame):
    assert len(game.get_all_bets()) == 0
    assert game.get_winning_pocket() is None


def test_add_bet(game: RouletteGame):
    bet = StraightUpBet(
        bet_amount=100,
        pocket=RoulettePocket(pocket_number=9),
    )
    game.add_bet(bet)
    assert len(game.get_all_bets()) == 1
    assert game.get_all_bets()[0] == bet


def test_clear_bets(game: RouletteGame):
    bet = StraightUpBet(
        bet_amount=100,
        pocket=RoulettePocket(pocket_number=1),
    )

    game.clear_bets()
    assert len(game.get_all_bets()) == 0


def test_pocket_from_coord(game: RouletteGame):
    pocket = game.pocket_from_coord(2, 3)  # This should correspond to pocket_number 1
    assert pocket.pocket_number == 6


def test_pockets_from_color(game: RouletteGame):
    red_pockets = game.pockets_from_color(PocketColor.RED)
    assert len(red_pockets) == 18
    assert red_pockets[0].pocket_color == PocketColor.RED

    black_pockets = game.pockets_from_color(PocketColor.BLACK)
    assert len(black_pockets) == 18
    assert black_pockets[0].pocket_color == PocketColor.BLACK
    green_pockets = game.pockets_from_color(PocketColor.GREEN)

    assert len(green_pockets) == 2
    assert green_pockets[0].pocket_color == PocketColor.GREEN


def test_straight_up_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = StraightUpBet(
        bet_amount=100,
        pocket=RoulettePocket(pocket_number=9),
    )
    game.add_bet(bet)

    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won == 3500


def test_split_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = SplitBet(
        bet_amount=100,
        pockets=[
            RoulettePocket(pocket_number=8),
            RoulettePocket(pocket_number=9),
        ],
    )
    game.add_bet(bet)

    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won == 1700


def test_street_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = StreetBet(
        bet_amount=100,
        pockets=[
            RoulettePocket(pocket_number=7),
            RoulettePocket(pocket_number=8),
            RoulettePocket(pocket_number=9),
        ],
    )
    game.add_bet(bet)

    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won == 1100


def test_five_number_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = FiveNumberBet(
        bet_amount=100,
    )
    game.add_bet(bet)
    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won is None


def test_line_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = LineBet(
        bet_amount=100,
        pockets=[
            RoulettePocket(pocket_number=7),
            RoulettePocket(pocket_number=8),
            RoulettePocket(pocket_number=9),
            RoulettePocket(pocket_number=10),
            RoulettePocket(pocket_number=11),
            RoulettePocket(pocket_number=12),
        ],
    )
    game.add_bet(bet)
    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won == 500


def test_dozen_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = DozenBet(
        bet_amount=100,
        bet=Dozen.FIRST_DOZEN,
    )
    game.add_bet(bet)
    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won == 200


def test_column_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = ColumnBet(
        bet_amount=100,
        bet=Column.THIRD_COLUMN,
    )
    game.add_bet(bet)
    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won == 200


def test_eighteen_number_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = EighteenNumberBet(
        bet_amount=100,
        bet=HighOrLow.LOW,
    )
    game.add_bet(bet)
    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won == 100


def test_color_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = ColorBet(
        bet_amount=100,
        bet=PocketColor.RED,
    )
    game.add_bet(bet)
    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won == 100


def test_odd_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = OddOrEvenBet(
        bet_amount=100,
        bet=RouletteBetType.ODD,
    )
    game.add_bet(bet)
    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won == 100


def test_even_bet(game: RouletteGame):
    game.winning_pocket = RoulettePocket(pocket_number=7)

    bet = OddOrEvenBet(
        bet_amount=100,
        bet=RouletteBetType.EVEN,
    )
    game.add_bet(bet)
    with patch("random.Random.randint", return_value=9):
        game.spin()

    assert game.get_winning_pocket().pocket_number == 9
    assert bet.amount_won is None
