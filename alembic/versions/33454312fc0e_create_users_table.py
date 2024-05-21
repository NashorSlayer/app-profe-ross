"""create users table

Revision ID: 33454312fc0e
Revises: 8cbcefb1c447
Create Date: 2024-05-19 01:40:08.437726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, INTEGER, VARCHAR


# revision identifiers, used by Alembic.
revision: str = '33454312fc0e'
down_revision: Union[str, None] = '8cbcefb1c447'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "users",
    Column("id", INTEGER, primary_key=True),
    Column("name", VARCHAR(255), nullable=False),
    Column("last_name", VARCHAR(255), nullable=False),
    Column("email", VARCHAR(255), nullable=False, unique=True),
    Column("password", VARCHAR(255), nullable=False),
)


def downgrade() -> None:
    op.drop_table("users")
