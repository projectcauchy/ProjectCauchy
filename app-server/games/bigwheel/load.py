import pandas as pd
from datetime import datetime

# TODO: Write to DB for production
def load(df: pd.DataFrame):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    df.to_csv(f"data/bigwheel_{now}.csv",index=False)
