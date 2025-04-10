"""empty message

Revision ID: 36ca71463257
Revises: 3ac74ae2e3c8
Create Date: 2025-04-10 20:34:30.924549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36ca71463257'
down_revision = '3ac74ae2e3c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('likes')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('likes', sa.INTEGER(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
