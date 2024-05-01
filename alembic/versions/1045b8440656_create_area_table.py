"""create area table

Revision ID: 1045b8440656
Revises: 1b94371c4f05
Create Date: 2024-05-01 09:56:33.185760

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column


# revision identifiers, used by Alembic.
revision: str = '1045b8440656'
down_revision: Union[str, None] = '1b94371c4f05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "area",
        Column("area_id", INTEGER, primary_key=True),
        Column("name", VARCHAR(255), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("area")
