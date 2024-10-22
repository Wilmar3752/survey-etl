from _settings import SURVEY
from arcgis.gis import GIS

portalURL = SURVEY['URL']
username = SURVEY['USERNAME']
password = SURVEY['PASSWORD']
survey_item_id = SURVEY['ITEM_ID']

gis = GIS(portalURL, username, password)
survey_by_id = gis.content.get(survey_item_id)

def get_feature_set(layer:int):
    # Get the related feature service
    feature_service_item = survey_by_id.related_items('Survey2Service','forward')[0]

    # Access the feature layer
    feature_layer = feature_service_item.layers[layer]
    
    # Query the feature layer and fetch all features
    feature_set = feature_layer.query()

    # Convert the feature set to a Pandas DataFrame
    df = feature_set.sdf

    # Display the DataFrame
    return df

def extract():
    df_list = [get_feature_set(i) for i in range(2)]
    return df_list