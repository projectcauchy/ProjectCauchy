import pandas as pd
from datetime import datetime

# TODO: Write to DB for production
def load(df: pd.DataFrame):
    df.to_csv(f"data/bigwheel_{datetime.now()}.csv",index=False)
