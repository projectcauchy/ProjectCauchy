import pandas as pd


def transform(records: list):
    records_df = pd.DataFrame(records)

    return records_df