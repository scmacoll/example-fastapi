"""create posts table

Revision ID: d387ce550aaf
Revises: 
Create Date: 2022-04-03 16:16:10.409964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd387ce550aaf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
        )
    pass

# undo
def downgrade():
    op.delete_table('posts')
    pass
