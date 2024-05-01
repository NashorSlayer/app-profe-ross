from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

# Define the table
users = Table(
    "user",meta,
    Column("user_id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("last_name", String(255)),
    Column("email", String(255),unique=True),
    Column("password", String(255)),
)