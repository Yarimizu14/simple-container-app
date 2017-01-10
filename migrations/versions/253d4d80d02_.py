"""empty message

Revision ID: 253d4d80d02
Revises: None
Create Date: 2017-01-10 08:06:46.551606

"""

# revision identifiers, used by Alembic.
revision = '253d4d80d02'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('messages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('message', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('messages')
