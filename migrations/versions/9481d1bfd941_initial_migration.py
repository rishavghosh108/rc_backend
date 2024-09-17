"""Initial migration.

Revision ID: 9481d1bfd941
Revises: 41a9092a460c
Create Date: 2024-09-16 02:40:58.612811

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9481d1bfd941'
down_revision = '41a9092a460c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('dob',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.Date(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('dob',
               existing_type=sa.Date(),
               type_=sa.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###