"""create survey_areas table

Revision ID: 8bb4c224c6ec
Revises: 97a3004f01c9
Create Date: 2024-05-19 01:46:47.669686

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, INTEGER, ForeignKey


# revision identifiers, used by Alembic.
revision: str = '8bb4c224c6ec'
down_revision: Union[str, None] = '97a3004f01c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "survey_areas",
        Column("id", INTEGER, primary_key=True),
        Column("area_id", INTEGER, ForeignKey("areas.id"), nullable=False),
        Column("survey_id", INTEGER, ForeignKey("surveys.id"), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("survey_areas")
