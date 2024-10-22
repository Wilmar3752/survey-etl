import os
from dotenv import load_dotenv

load_dotenv()
SURVEY = {
    'URL': os.environ['SURVEY_URL'],
    'USERNAME': os.environ['SURVEY_USERNAME'],
    'PASSWORD': os.environ['SURVEY_PASSWORD'],
    'ITEM_ID': os.environ['SURVEY_ITEM_ID']
}

DATABASE_CONFIG = {
    "dbname": os.environ['DB_NAME'],
    "user":  os.environ['USER_NAME'],
    "password":  os.environ['PASSWORD'],
    "host":  os.environ['HOST'],
    "port": os.environ['PORT']
}