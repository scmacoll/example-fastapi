"""add content column to posts table

Revision ID: e7288740cd97
Revises: d387ce550aaf
Create Date: 2022-04-06 21:34:26.428603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7288740cd97'
down_revision = 'd387ce550aaf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',
        sa.Column('content', sa.String(), nullable=False)
        )
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
