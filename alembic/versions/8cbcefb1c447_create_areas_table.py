"""create areas table

Revision ID: 8cbcefb1c447
Revises: 
Create Date: 2024-05-19 01:38:29.325351

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Column, INTEGER, VARCHAR


# revision identifiers, used by Alembic.
revision: str = '8cbcefb1c447'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "areas",
        Column("id", INTEGER, primary_key=True),
        Column("name", VARCHAR(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("areas")
