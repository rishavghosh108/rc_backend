"""Initial migration.

Revision ID: 905a3bd521e2
Revises: ea58c4a390a5
Create Date: 2024-09-16 05:17:19.723411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '905a3bd521e2'
down_revision = 'ea58c4a390a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('token',
    sa.Column('id', sa.NullType(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('token', sa.NullType(), nullable=False),
    sa.Column('date', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    # ### end Alembic commands ###
