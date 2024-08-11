import os
import sys

# Add the parent directory of 'games' (i.e., 'app-server') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
load_dotenv()
URL = os.getenv('DEV_HOST')

# Import modules
from games.bigwheel import pipeline_bigwheel
from games.roulette import roulette_pipeline
from games.baccarat import pipeline_baccarat


pipeline_baccarat()

roulette_pipeline()

pipeline_bigwheel(URL)
