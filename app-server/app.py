import sys
from pathlib import Path
from fastapi import FastAPI
sys.path.append(str(Path(__file__).resolve().parent.parent))
from game_server.poker.routes import router as poker_router

app = FastAPI()
app.include_router(poker_router)
