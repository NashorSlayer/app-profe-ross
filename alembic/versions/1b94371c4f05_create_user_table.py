"""create user table

Revision ID: 1b94371c4f05
Revises: 
Create Date: 2024-05-01 00:20:50.869440

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import INTEGER, VARCHAR, NVARCHAR, Column


# revision identifiers, used by Alembic.
revision: str = '1b94371c4f05'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "user",
    Column("user_id", INTEGER, primary_key=True),
    Column("name", VARCHAR(255), nullable=False),
    Column("last_name", VARCHAR(255), nullable=False),
    Column("email", VARCHAR(255), nullable=False, unique=True),
    Column("password", VARCHAR(255), nullable=False),
)


def downgrade() -> None:
    op.drop_table("user")
