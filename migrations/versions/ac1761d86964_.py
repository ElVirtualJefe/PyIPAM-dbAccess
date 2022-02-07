"""empty message

Revision ID: ac1761d86964
Revises: b30bd1bfc37d
Create Date: 2021-09-27 22:34:35.945658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac1761d86964'
down_revision = 'b30bd1bfc37d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('category', sa.String(length=24), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'category')
    # ### end Alembic commands ###