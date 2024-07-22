from fastapi import FastAPI
from games.poker import simulate_poker
from games.bigwheel import simulate_bigwheel
from games.baccarat import simulate_baccarat
from dataclasses import asdict

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


# @app.get("/baccarat/multiple")
# def get_baccarat_single(n_games: int):
#     return asdict(simulate_baccarat)