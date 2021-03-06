"""novos intens corrigidos e alterados

Revision ID: 37b7bfcd1d7b
Revises: 45003b5d3a09
Create Date: 2021-06-01 21:10:27.303601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37b7bfcd1d7b'
down_revision = '45003b5d3a09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('empresa', schema=None) as batch_op:
        batch_op.drop_constraint('fk_passagem', type_='foreignkey')
        batch_op.drop_column('passagem_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('empresa', schema=None) as batch_op:
        batch_op.add_column(sa.Column('passagem_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_passagem', 'passagem', ['passagem_id'], ['id'])

    # ### end Alembic commands ###
