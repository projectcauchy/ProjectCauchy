import pandas as pd
from .extract import extract
from .transform import transform
from .load import load


def pipeline_baccarat():
    
    baccarat_json = extract(game = 'baccarat', n = 10)
    print('Extraction completed')
    
    baccarat_df = transform(baccarat_json)
    print('Transformation completed')

    load(baccarat_df)
    print('Loading completed')

    