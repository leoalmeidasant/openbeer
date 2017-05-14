"""empty message

Revision ID: 8aa000fdcf90
Revises: c52b7fa3b6fb
Create Date: 2017-05-13 18:49:42.652559

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8aa000fdcf90'
down_revision = 'c52b7fa3b6fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('delivery_address_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_orders_delivery_address_id'), 'orders', ['delivery_address_id'], unique=False)
    op.create_foreign_key(None, 'orders', 'address', ['delivery_address_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'orders', type_='foreignkey')
    op.drop_index(op.f('ix_orders_delivery_address_id'), table_name='orders')
    op.drop_column('orders', 'delivery_address_id')
    # ### end Alembic commands ###