from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
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
Session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
metadata = Base.metadata