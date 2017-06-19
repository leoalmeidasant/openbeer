"""empty message

Revision ID: 33803d062d93
Revises: c66406de4ef1
Create Date: 2017-06-10 20:11:36.825696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33803d062d93'
down_revision = 'c66406de4ef1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('gender', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'gender')
    # ### end Alembic commands ###
