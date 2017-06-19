"""empty message

Revision ID: ef268eb48b33
Revises: eb0d55894cb9
Create Date: 2017-06-18 20:43:54.205682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef268eb48b33'
down_revision = 'eb0d55894cb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item_orders', sa.Column('traded', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item_orders', 'traded')
    # ### end Alembic commands ###
