import sys
from pathlib import Path
from fastapi import FastAPI

# For importing modules outside the folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import poker game routes from poker route module
from game_server.poker.routes import router as poker_router

# Instance of FastAPI
app = FastAPI()

# Include the Poker routes in the FastAPI application
app.include_router(poker_router)
