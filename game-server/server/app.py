from fastapi import FastAPI
from games.poker.sim import simulate
from dataclasses import asdict

app = FastAPI()

# Define a route that returns a JSON response
@app.get("/poker")
def get_info():
    return asdict(simulate())
