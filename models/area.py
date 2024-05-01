from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

# Define the table
areas = Table(
    "area",meta,
    Column("area_id", Integer, primary_key=True),
    Column("name", String(255)),
)