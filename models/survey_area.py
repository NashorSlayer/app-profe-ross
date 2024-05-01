from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, ForeignKey
from config.db import meta

# Define the table
answer_area = Table(
    "answer_area",meta,
    Column("answer_area_id", Integer, primary_key=True),
    Column("area_id", String(255), ForeignKey("area.area_id")),
    Column("survey_id", String(255),ForeignKey("survey.survey_id")),
)