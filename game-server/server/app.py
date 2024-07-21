from fastapi import FastAPI
from games.poker import simulate_poker
from games.bigwheel import simulate_bigwheel
from dataclasses import asdict

app = FastAPI()

@app.get("/poker")
def get_poker():
    return asdict(simulate_poker())

@app.get("/bigwheel")
def get_bigwheel():
    return asdict(simulate_bigwheel())
