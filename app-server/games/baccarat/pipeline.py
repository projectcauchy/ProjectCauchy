import pandas as pd
from .extract import extract
from .transform import transform
from .load import load


def pipeline_baccarat():
    extract()
    transform()
    load()
    print('Pipeline completed')