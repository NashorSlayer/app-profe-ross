"""create surveys table

Revision ID: 97a3004f01c9
Revises: 33454312fc0e
Create Date: 2024-05-19 01:41:09.486555

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from sqlalchemy import Column, INTEGER, VARCHAR , ForeignKey

# revision identifiers, used by Alembic.
revision: str = '97a3004f01c9'
down_revision: Union[str, None] = '33454312fc0e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "surveys",
        Column("id", INTEGER, primary_key=True),
        Column("name", VARCHAR(255), nullable=False),
        Column("description", VARCHAR(255), nullable=False),
        Column("time_range_start", VARCHAR(255), nullable=False),
        Column("time_range_end", VARCHAR(255), nullable=False),
        Column ("answer_time_start", VARCHAR(255), nullable=False),
        Column ("answer_time_end", VARCHAR(255), nullable=False),
        Column("user_id", INTEGER, ForeignKey("users.id"),nullable=False),
    )


def downgrade() -> None:
    op.drop_table("surveys")
