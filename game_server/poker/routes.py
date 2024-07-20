from fastapi import APIRouter
from .poker_game_logic import generate_poker_hand

router = APIRouter()


@router.get("/poker")
def get_poker_hand():
    poker_hand_response = generate_poker_hand()
    return poker_hand_response
