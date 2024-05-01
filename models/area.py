from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import conn, meta

#Define the table
areas = Table(
    "areas", meta,
    Column("area_id", Integer, primary_key=True),
    Column("name", String(255)),
)


# Create the table
meta.create_all(conn)