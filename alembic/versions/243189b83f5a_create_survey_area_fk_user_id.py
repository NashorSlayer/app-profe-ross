"""create survey area (FK user_id)

Revision ID: 243189b83f5a
Revises: 1045b8440656
Create Date: 2024-05-01 10:02:47.072967

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column, ForeignKey



# revision identifiers, used by Alembic.
revision: str = '243189b83f5a'
down_revision: Union[str, None] = '1045b8440656'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "survey",
        Column("survey_id", INTEGER, primary_key=True),
        Column("name", VARCHAR(255), nullable=False),
        Column("description", VARCHAR(255), nullable=False),
        Column("time_range_init", VARCHAR(255), nullable=False),
        Column("time_range_end", VARCHAR(255), nullable=False),
        Column ("answer_time_init", VARCHAR(255), nullable=False),
        Column ("answer_time_end", VARCHAR(255), nullable=False),
        Column("user_id", INTEGER, ForeignKey("user.user_id"),nullable=False),
    )


def downgrade() -> None:
    op.drop_table("survey")
