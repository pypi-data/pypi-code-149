"""Ajout vigilance meteo

Revision ID: 901a31d192ad
Revises: dcffac33e4fd
Create Date: 2021-11-26 16:35:51.243300

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '901a31d192ad'
down_revision = 'dcffac33e4fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vigilance_meteo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('zone_id', sa.Integer(), nullable=True),
    sa.Column('phenomene_id', sa.Integer(), nullable=True),
    sa.Column('date_export', sa.DateTime(), nullable=True),
    sa.Column('couleur_id', sa.Integer(), nullable=True),
    sa.Column('validity', postgresql.TSTZRANGE(), nullable=False),
    sa.Column('to_show', postgresql.DATERANGE(), nullable=False),
    sa.ForeignKeyConstraint(['zone_id'], ['indice_schema.zone.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='indice_schema'
    )
    op.create_index('vigilance_zone_phenomene_date_export_idx', 'vigilance_meteo', ['zone_id', 'phenomene_id', 'date_export'], unique=False, schema='indice_schema')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('vigilance_zone_phenomene_date_export_idx', table_name='vigilance_meteo', schema='indice_schema')
    op.drop_table('vigilance_meteo', schema='indice_schema')
    # ### end Alembic commands ###
