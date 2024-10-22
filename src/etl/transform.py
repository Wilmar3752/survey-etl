import pandas as pd
import json
import logging
import sys

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)

def transform(list_df:list):
    logger.info('Tranforming data to be writted in database')
    list_df_transformed = [lower_colnames(df) for df in list_df]
    list_df_transformed[0] = list_df_transformed[0].drop('shape', axis=1)
    list_df_transformed[1]['shape'] = list_df_transformed[1]['shape'].apply(point_to_json)
    return list_df_transformed

def lower_colnames(df: pd.DataFrame):
    df.columns = df.columns.str.lower()
    return df

def point_to_json(point):
    return json.dumps({
        'type': 'Point',
        'coordinates': [point['x'], point['y']],
        'spatialReference': {'wkid': point['spatialReference']['wkid']}
    })