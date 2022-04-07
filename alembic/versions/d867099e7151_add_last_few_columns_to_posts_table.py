"""add last few columns to posts table

Revision ID: d867099e7151
Revises: 7e072b8631fd
Create Date: 2022-04-07 13:58:03.559297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd867099e7151'
down_revision = '7e072b8631fd'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published', sa.Boolean(), nullable=False, server_default="TRUE")),
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')) )
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
