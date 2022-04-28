"""empty message

Revision ID: e052247a4800
Revises: afc9193d5664
Create Date: 2022-04-28 09:26:10.979545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e052247a4800'
down_revision = 'afc9193d5664'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subnets', sa.Column('dateCreated', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subnets', 'dateCreated')
    # ### end Alembic commands ###