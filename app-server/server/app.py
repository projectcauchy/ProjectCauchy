import os
import sys
import pandas as pd

# Add the parent directory of 'games' (i.e., 'app-server') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import modules
from games.baccarat import pipeline_baccarat 


pipeline_baccarat()
