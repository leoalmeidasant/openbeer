"""empty message

Revision ID: c161011abf5e
Revises: af661bd45c61
Create Date: 2017-05-07 14:41:11.815179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c161011abf5e'
down_revision = 'af661bd45c61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_items_item_id'), 'items', ['item_id'], unique=False)
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fare', sa.Float(), nullable=True),
    sa.Column('order_date', sa.DateTime(), nullable=True),
    sa.Column('payment_form', sa.String(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_client_id'), 'orders', ['client_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orders_client_id'), table_name='orders')
    op.drop_table('orders')
    op.drop_index(op.f('ix_items_item_id'), table_name='items')
    op.drop_table('items')
    # ### end Alembic commands ###
