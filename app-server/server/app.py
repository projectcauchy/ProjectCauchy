import os
import sys

# Add the parent directory of 'games' (i.e., 'app-server') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
load_dotenv()
URL = os.getenv('DEV_HOST')

# Import modules
from games.bigwheel import pipeline_bigwheel

pipeline_bigwheel(URL)
