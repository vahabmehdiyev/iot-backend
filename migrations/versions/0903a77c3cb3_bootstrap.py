"""bootstrap

Revision ID: 0903a77c3cb3
Revises: 
Create Date: 2025-09-22 11:17:18.805801

"""
from typing import Sequence, Union


# revision identifiers, used by Alembic.
revision: str = '0903a77c3cb3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
