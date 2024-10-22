from src._settings import SURVEY
from arcgis.gis import GIS
import logging
import sys

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)

logger = logging.getLogger(__name__)


portalURL = SURVEY['URL']
username = SURVEY['USERNAME']
password = SURVEY['PASSWORD']
survey_item_id = SURVEY['ITEM_ID']

gis = GIS(portalURL, username, password)
survey_by_id = gis.content.get(survey_item_id)

def get_feature_set(layer:int):
    logger.info("Getting data from survey123")
    feature_service_item = survey_by_id.related_items('Survey2Service','forward')[0]
    feature_layer = feature_service_item.layers[layer]
    feature_set = feature_layer.query()
    df = feature_set.sdf
    return df

def extract():
    df_list = [get_feature_set(i) for i in range(2)]
    logger.info("Extraction finished")
    return df_list