"""insert feedback table

Revision ID: 74aad5fd518c
Revises: 806406eb69c3
Create Date: 2024-06-08 18:26:44.287029

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74aad5fd518c'
down_revision: Union[str, None] = '806406eb69c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("INSERT INTO feedback (id,email,rating) values(1,'kubilk56@gmail.com',4)")


def downgrade() -> None:
    pass
