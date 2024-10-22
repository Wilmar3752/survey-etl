from src._settings import DATABASE_CONFIG
from sqlalchemy import create_engine


# Define connection parameters
dbname = DATABASE_CONFIG['dbname']
user = DATABASE_CONFIG['user']
password = DATABASE_CONFIG['password']
host = DATABASE_CONFIG['host']
port = DATABASE_CONFIG['port']

# Create an engine
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{dbname}")
