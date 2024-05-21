"""create answer_areas table

Revision ID: c2e6400adaa6
Revises: 8bb4c224c6ec
Create Date: 2024-05-19 01:48:26.311908

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, INTEGER, ForeignKey


# revision identifiers, used by Alembic.
revision: str = 'c2e6400adaa6'
down_revision: Union[str, None] = '8bb4c224c6ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "answer_areas",
        Column("id", INTEGER, primary_key=True),
        Column("area_id", INTEGER, ForeignKey("areas.id"), nullable=False),
        Column("survey_id", INTEGER, ForeignKey("surveys.id"), nullable=False),
        Column("time", INTEGER, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("answer_areas")
