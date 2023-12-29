"""test revision1

Revision ID: 42255688d690
Revises: ca785ab8d750
Create Date: 2023-12-13 20:48:33.800786

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42255688d690'
down_revision: Union[str, None] = 'ca785ab8d750'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
