import sys

# Add the parent directory of 'games' (i.e., 'app-server') to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
load_dotenv()
URL = os.getenv('DEV_HOST')

# Import pipeline_baccarat from the games.baccarat module
from games.bigwheel.pipeline import pipeline_bigwheel

# Run the pipelinepipeline_bigwheel(URLn = 100000)
