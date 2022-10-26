"""empty message

Revision ID: f1967e3bb7ae
Revises: 
Create Date: 2022-10-26 13:32:17.831992

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1967e3bb7ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('district')
    op.add_column('point', sa.Column('area_id', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'point', type_='foreignkey')
    op.create_foreign_key(None, 'point', 'area', ['area_id'], ['id'])
    op.drop_column('point', 'district_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('point', sa.Column('district_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'point', type_='foreignkey')
    op.create_foreign_key(None, 'point', 'district', ['district_id'], ['id'])
    op.drop_column('point', 'area_id')
    op.create_table('district',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), nullable=True),
    sa.Column('latitude', sa.FLOAT(), nullable=True),
    sa.Column('longitude', sa.FLOAT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('area')
    # ### end Alembic commands ###