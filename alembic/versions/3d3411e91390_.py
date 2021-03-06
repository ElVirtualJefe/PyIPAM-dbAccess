"""empty message

Revision ID: 3d3411e91390
Revises: 3d117ede7e63
Create Date: 2022-04-28 11:41:30.836184

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3d3411e91390'
down_revision = '3d117ede7e63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('addressStates', 'id',
               existing_type=postgresql.UUID(),
               server_default=sa.text('uuid_generate_v4()'),
               existing_nullable=False)
    op.alter_column('ipAddresses', 'id',
               existing_type=postgresql.UUID(),
               server_default=sa.text('uuid_generate_v4()'),
               existing_nullable=False)
    op.alter_column('ipAddresses', 'state_id',
               existing_type=postgresql.UUID(),
               server_default=sa.text("CAST('5a3be258-876b-4fb3-9788-61acced67be1' AS UUID)"),
               existing_nullable=False)
    op.alter_column('ipAddresses', 'dateLastSeen',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
    op.alter_column('ipAddresses', 'dateLastEdited',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
    op.alter_column('settings', 'id',
               existing_type=postgresql.UUID(),
               server_default=sa.text('uuid_generate_v4()'),
               existing_nullable=False)
    op.alter_column('subnets', 'allowRequests',
               existing_type=sa.BOOLEAN(),
               server_default=sa.text('false'),
               existing_nullable=False)
    op.alter_column('subnets', 'dateLastEdited',
               existing_type=postgresql.TIMESTAMP(),
               server_default=sa.text('now()'),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
    op.alter_column('subnets', 'dateLastScanned',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
    op.alter_column('subnets', 'dateLastDiscovered',
               existing_type=postgresql.TIMESTAMP(),
               server_default=None,
               type_=sa.DateTime(timezone=True),
               existing_nullable=True)
    op.alter_column('subnets', 'doDiscovery',
               existing_type=sa.BOOLEAN(),
               server_default=sa.text('false'),
               existing_nullable=True)
    op.alter_column('subnets', 'doScan',
               existing_type=sa.BOOLEAN(),
               server_default=sa.text('false'),
               existing_nullable=True)
    op.alter_column('vlans', 'id',
               existing_type=postgresql.UUID(),
               server_default=sa.text('uuid_generate_v4()'),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('vlans', 'id',
               existing_type=postgresql.UUID(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('subnets', 'doScan',
               existing_type=sa.BOOLEAN(),
               server_default=None,
               existing_nullable=True)
    op.alter_column('subnets', 'doDiscovery',
               existing_type=sa.BOOLEAN(),
               server_default=None,
               existing_nullable=True)
    op.alter_column('subnets', 'dateLastDiscovered',
               existing_type=sa.DateTime(timezone=True),
               server_default=sa.text('now()'),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('subnets', 'dateLastScanned',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('subnets', 'dateLastEdited',
               existing_type=sa.DateTime(timezone=True),
               server_default=None,
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('subnets', 'allowRequests',
               existing_type=sa.BOOLEAN(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('settings', 'id',
               existing_type=postgresql.UUID(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('ipAddresses', 'dateLastEdited',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('ipAddresses', 'dateLastSeen',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True)
    op.alter_column('ipAddresses', 'state_id',
               existing_type=postgresql.UUID(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('ipAddresses', 'id',
               existing_type=postgresql.UUID(),
               server_default=None,
               existing_nullable=False)
    op.alter_column('addressStates', 'id',
               existing_type=postgresql.UUID(),
               server_default=None,
               existing_nullable=False)
    # ### end Alembic commands ###
