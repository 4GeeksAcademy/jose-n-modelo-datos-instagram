"""empty message

Revision ID: 14cffdef0e41
Revises: a445b39698bb
Create Date: 2025-04-10 23:50:06.862005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14cffdef0e41'
down_revision = 'a445b39698bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.add_column(sa.Column('post_id_2', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'post', ['post_id_2'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('media', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('post_id_2')

    # ### end Alembic commands ###
