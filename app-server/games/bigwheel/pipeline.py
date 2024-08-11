from .extract import extract
from .load import load
from utils import logger

def pipeline_bigwheel(url):
    bwheel = extract(url)
    load(bwheel)
    logger.info('Pipeline completed')
