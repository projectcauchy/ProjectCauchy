import sys
import os

# Add the parent directory of 'games' (i.e., 'app-server') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import pipeline_baccarat from the games.baccarat module
from games.baccarat.pipeline import pipeline_baccarat 

# Run the pipeline
pipeline_baccarat(n = 100000)
