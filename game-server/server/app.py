from fastapi import FastAPI, Query
from games.poker import simulate_poker
from games.bigwheel import simulate_bigwheel
from games.baccarat import simulate_baccarat
from games.blackjack import simulate_blackjack_games
from dataclasses import asdict
from typing import Dict, Any

app = FastAPI()

@app.get("/poker")
def get_poker():
    return asdict(simulate_poker())

@app.get("/bigwheel")
def get_bigwheel():
    return asdict(simulate_bigwheel())


@app.get("/baccarat")
def get_baccarat_single():
    return asdict(simulate_baccarat())

@app.get("/blackjack")
def get_blackjack(
    players: int = Query(default=10, ge=1, le=10000),
    games: int = Query(default=10, ge=1, le=100000)
) -> Dict[str, Any]:
    simulation = simulate_blackjack_games(players, games)
    return asdict(simulation)
