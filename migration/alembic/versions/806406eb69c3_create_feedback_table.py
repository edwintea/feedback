"""create feedback table

Revision ID: 806406eb69c3
Revises: 
Create Date: 2024-06-08 18:23:36.320811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '806406eb69c3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "feedback",
        sa.Column("id",sa.Integer,primary_key=True),
        sa.Column("email",sa.String(50),nullable=False),
        sa.Column("rating",sa.Integer,nullable=False)
    )


def downgrade() -> None:
    op.drop_table("feedback")
