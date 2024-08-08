import pandas as pd


def load(records_df: pd.DataFrame):
    records_df.to_csv('games/baccarat/baccarat_records.csv')