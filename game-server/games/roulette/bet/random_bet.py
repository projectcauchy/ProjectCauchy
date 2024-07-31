from random import Random
from ..game import RouletteGame, PocketColor
from . import (
    RouletteBet,
    RouletteBetType,
    EighteenNumberBetType,
    ColumnBetType,
    DozenBetType,
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
)


def random_bet(game: RouletteGame) -> RouletteBet:
    bet_type: RouletteBetType = Random().choice(list(RouletteBetType))
    if bet_type is RouletteBetType.STRAIGHT_UP:
        return _random_straight_up_bet(game)

    if bet_type is RouletteBetType.SPLIT:
        return _random_split_bet(game)

    if bet_type is RouletteBetType.STREET:
        return _random_street_bet(game)

    if bet_type is RouletteBetType.FIVE_NUMBER_BET:
        return _five_number_bet(game)

    if bet_type is RouletteBetType.LINE:
        return _random_line_bet(game)

    if bet_type is RouletteBetType.DOZEN:
        return _random_dozen_bet(game)

    if bet_type is RouletteBetType.COLUMN:
        return _random_column_bet(game)

    if bet_type is RouletteBetType.EIGHTEEN_NUMBER_BET:
        return _random_eighteen_number_bet(game)

    if bet_type is RouletteBetType.COLOR:
        return _random_color_bet(game)

    if bet_type is RouletteBetType.ODD:
        return _odd_or_even_bet(game=game, is_even=False)

    if bet_type is RouletteBetType.EVEN:
        return _odd_or_even_bet(game=game, is_even=True)


def _random_straight_up_bet(game: RouletteGame) -> RouletteBet:
    row = Random().randint(1, 12)
    col = Random().randint(1, 3)
    random_pocket = game.pocket_from_coord(row, col)

    return StraightUpBet(
        bet_amount=Random().uniform(1, 100),
        pocket=random_pocket,
    )


def _random_split_bet(game: RouletteGame) -> RouletteBet:
    row = Random().randint(1, 12)
    col = Random().randint(1, 3)
    random_pocket = game.pocket_from_coord(row, col)
    adj_rows = [i for i in [row - 1, row + 1] if i >= 1 and i <= 12]
    adj_cols = [i for i in [col - 1, col + 1] if i >= 1 and i <= 3]

    should_use_row = Random().random() < 0.5

    cell = Random().choice(adj_rows) if should_use_row else Random().choice(adj_cols)
    adj_row, adj_col = (cell, col) if should_use_row else (row, cell)

    adjacent_pocker = game.pocket_from_coord(adj_row, adj_col)
    return SplitBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[random_pocket, adjacent_pocker],
    )


def _random_street_bet(game: RouletteGame) -> RouletteBet:
    row = Random().randint(1, 12)
    return StreetBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[game.pocket_from_coord(row, col) for col in range(1, 4)],
    )


def _five_number_bet(game: RouletteGame) -> RouletteBet:
    return FiveNumberBet(
        bet_amount=Random().uniform(1, 100),
    )


def _random_line_bet(game: RouletteGame) -> RouletteBet:
    row = Random().randint(1, 11)
    return LineBet(
        bet_amount=Random().uniform(1, 100),
        pockets=[game.pocket_from_coord(row, col) for col in range(1, 4)]
        + [game.pocket_from_coord(row + 1, col) for col in range(1, 4)],
    )


def _random_dozen_bet(game: RouletteGame) -> RouletteBet:
    bet = Random().choice(list(DozenBetType))
    return DozenBet(
        bet_amount=Random().uniform(1, 100),
        bet=bet,
    )


def _random_column_bet(game: RouletteGame) -> RouletteBet:
    bet = Random().choice(list(ColumnBetType))
    return ColumnBet(
        bet_amount=Random().uniform(1, 100),
        bet=bet,
    )


def _random_eighteen_number_bet(game: RouletteGame) -> RouletteBet:
    bet = Random().choice(list(EighteenNumberBetType))
    return EighteenNumberBet(
        bet_amount=Random().uniform(1, 100),
        bet=bet,
    )


def _random_color_bet(game: RouletteGame) -> RouletteBet:
    color = Random().choice(list(PocketColor))

    return ColorBet(
        bet_amount=Random().uniform(1, 100),
        bet=color,
    )


def _odd_or_even_bet(game: RouletteGame, is_even: bool) -> RouletteBet:
    bet = Random().choice([RouletteBetType.ODD, RouletteBetType.EVEN])
    return OddOrEvenBet(
        bet_amount=Random().uniform(1, 100),
        bet=bet,
    )
