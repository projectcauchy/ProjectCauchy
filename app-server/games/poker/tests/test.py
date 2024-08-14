import pytest
import pandas as pd
from unittest.mock import patch, MagicMock
from ..extract import extract_poker
from ..transform import transform_data
from ..load import save_dataframes
import os

sample_json_data = [{
    "gameID": "c688916bf5e4070eb68c6ade",
    "datetime_start": "2024-08-13 15:08:34",
    "datetime_end": "2024-08-13 15:48:34",
    "employeeDealerId": "p6q7r8",
    "totalRounds": 4,
    "winType": "showdown",
    "winner": "e5dcf3bdbd660fff6fb1939e0",
    "totalPot": 39462,
    "initialBlind": 10,
    "rake": 5,
    "players": [
        {
            "playerId": "e5dcf3bdbd660fff6fb1939e0",
            "holeCards": [{"rank": "J", "suit": "D"}, {"rank": "6", "suit": "S"}],
            "startingChips": 37663,
            "bestHand": "tp",
            "netWin": 3443.90
        },
        {
            "playerId": "1200a7bad549b138b0362a347",
            "holeCards": [{"rank": "8", "suit": "D"}, {"rank": "4", "suit": "C"}],
            "startingChips": 5407,
            "bestHand": "tp",
            "netWin": -5417
        }
    ],
    "communityCards": {
        "flop": [{"rank": "3", "suit": "S"}, {"rank": "9", "suit": "S"}, {"rank": "9", "suit": "C"}],
        "turn": {"rank": "3", "suit": "C"},
        "river": {"rank": "2", "suit": "S"}
    }
}]


@patch('requests.get')
def test_extract_poker(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = sample_json_data
    mock_get.return_value = mock_response

    result = extract_poker(poker_hands=1, env='development')
    assert result is not None
    assert len(result) == 1
    assert 'gameID' in result[0]


def test_transform_data():
    games_df, players_df, game_players_df, community_cards_df, hole_cards_df = transform_data(sample_json_data)
    assert not games_df.empty
    assert not players_df.empty
    assert not game_players_df.empty
    assert not community_cards_df.empty
    assert not hole_cards_df.empty
    assert 'gameID' in games_df.columns
    assert 'playerID' in players_df.columns
    assert 'startingChips' in game_players_df.columns
    assert 'flopRank' in community_cards_df.columns
    assert 'cardRank_1' in hole_cards_df.columns


def test_save_dataframes(tmpdir):
    # Use the sample JSON data directly since extract_poker is mocked
    games_df, players_df, game_players_df, community_cards_df, hole_cards_df = transform_data(sample_json_data)
    output_dir = tmpdir.mkdir("poker_csv")
    save_dataframes(games_df, players_df, game_players_df, community_cards_df, hole_cards_df, output_dir=str(output_dir))
    assert os.path.isfile(os.path.join(output_dir, 'games.csv'))
    assert os.path.isfile(os.path.join(output_dir, 'players.csv'))
    assert os.path.isfile(os.path.join(output_dir, 'game_players.csv'))
    assert os.path.isfile(os.path.join(output_dir, 'community_cards.csv'))
    assert os.path.isfile(os.path.join(output_dir, 'hole_cards.csv'))
    games_df_read = pd.read_csv(os.path.join(output_dir, 'games.csv'))
    assert not games_df_read.empty
    assert 'gameID' in games_df_read.columns
