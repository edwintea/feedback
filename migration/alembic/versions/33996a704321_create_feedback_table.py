"""create feedback table

Revision ID: 33996a704321
Revises: a113d3d9a08f
Create Date: 2024-06-07 13:55:55.468537

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33996a704321'
down_revision: Union[str, None] = 'a113d3d9a08f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "feedback",
        sa.Column("id",sa.Integer,primary_key=True),
        sa.Column("name",sa.String(50),nullable=False),
        sa.Column("email",sa.String(50),nullable=False),
        sa.Column("rating",sa.Integer,nullable=False)
    )


def downgrade() -> None:
    op.drop_table("feedback")
