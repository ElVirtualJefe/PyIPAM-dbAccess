"""empty message

Revision ID: b3b95c391e69
Revises: 2d349a41c657
Create Date: 2022-04-27 19:10:53.246506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3b95c391e69'
down_revision = '2d349a41c657'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subnets', sa.Column('displayName', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subnets', 'displayName')
    # ### end Alembic commands ###
