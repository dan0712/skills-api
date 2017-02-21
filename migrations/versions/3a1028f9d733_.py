"""empty message

Revision ID: 3a1028f9d733
Revises: 4c7ffc4b5b09
Create Date: 2016-07-16 23:46:17.911297

"""

# revision identifiers, used by Alembic.
revision = '3a1028f9d733'
down_revision = '4c7ffc4b5b09'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('jobs_alternate_titles', sa.Column('nlp_a', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('jobs_alternate_titles', 'nlp_a')
    ### end Alembic commands ###
