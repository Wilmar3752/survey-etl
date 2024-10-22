import pandas as pd
import logging
import sys

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)
def load(engine, list_df):
    logger.info(f'Loading data to postgres: {list_df[0].shape[0]}')
    list_df[0].to_sql(name = "fact_sample",con = engine, schema = "survey", if_exists = 'replace', index=False)
    list_df[1].to_sql(name = "dim_sample",con = engine, schema = "survey", if_exists = 'replace', index=False)
