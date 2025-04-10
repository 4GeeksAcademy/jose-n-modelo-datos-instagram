"""empty message

Revision ID: b130a5d60722
Revises: 44385f3b8974
Create Date: 2025-04-10 21:18:35.220380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b130a5d60722'
down_revision = '44385f3b8974'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follower',
    sa.Column('user_from_id', sa.Integer(), nullable=False),
    sa.Column('user_to_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_from_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_to_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_from_id', 'user_to_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('follower')
    # ### end Alembic commands ###
