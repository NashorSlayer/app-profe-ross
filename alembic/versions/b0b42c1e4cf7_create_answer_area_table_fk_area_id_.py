"""create answer_area table (FK area_id, survey_id)

Revision ID: b0b42c1e4cf7
Revises: 8c252b49523f
Create Date: 2024-05-01 13:01:21.631973

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column,INTEGER, ForeignKey


# revision identifiers, used by Alembic.
revision: str = 'b0b42c1e4cf7'
down_revision: Union[str, None] = '8c252b49523f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "answer_area",
        Column("answer_area_id", INTEGER, primary_key=True),
        Column("area_id", INTEGER, ForeignKey("area.area_id"), nullable=False),
        Column("survey_id", INTEGER, ForeignKey("survey.survey_id"), nullable=False),
        Column("time", INTEGER, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("answer_area")
