import pandas as pd
from .extract import extract
from .transform import transform
from .load import load
from utils import logger


def pipeline_baccarat(url):

    error = 0
    try:
        baccarat_json = extract(url)
        logger.info('Baccarat data extraction completed')
    except:
        error += 1
        logger.info('Error in Baccarat data extraction')
    
    try:
        baccarat_data = transform(baccarat_json)
        logger.info('Baccarat data transformation completed')
    except:
        error += 1
        logger.info('Error in Baccarat data transformation')

    try:
        load(baccarat_data)
        logger.info('Baccarat data loading completed')
    except:
        error += 1
        logger.info('Error in Baccarat data loading')

    logger.info(f'Baccarat pipeline completed with {error} error/s')