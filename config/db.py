from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from decouple import config

# mysql settings
mysql_user = config('MYSQL_USER')
mysql_password = config('MYSQL_PASSWORD')
mysql_host = config('MYSQL_HOST')
mysql_port = config('MYSQL_PORT')
mysql_db = config('MYSQL_DB')
url_sql = f'mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_db}'

# create engine and connection
engine = create_engine(url_sql, echo=True)


# create metadata
meta = MetaData()


conn = engine.connect()

