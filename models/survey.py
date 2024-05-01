from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, ForeignKey
from config.db import meta

# Define the table
surveys = Table(
    "survey",meta,
    Column("survey_id", Integer, primary_key=True),
    Column("name", String(255), nullable=False), 
    Column("description", String(255), nullable=False),
    Column("time_range_init", String(255),nullable=False),
    Column("time_range_end", String(255), nullable=False),
    Column("answer_time_init", String(255), nullable=False),
    Column("answer_time_end", String(255), nullable=False),
    Column("user_id", Integer(255), ForeignKey("user.user_id"), nullable=False),
)