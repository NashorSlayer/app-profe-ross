"""create survey_area table (FK area_id,survey_id)

Revision ID: 8c252b49523f
Revises: 243189b83f5a
Create Date: 2024-05-01 11:00:58.282698

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey


# revision identifiers, used by Alembic.
revision: str = '8c252b49523f'
down_revision: Union[str, None] = '243189b83f5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "survey_area",
        Column("survey_area_id", INTEGER, primary_key=True),
        Column("area_id", INTEGER, ForeignKey("area.area_id"), nullable=False),
        Column("survey_id", INTEGER, ForeignKey("survey.survey_id"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("survey_area")
