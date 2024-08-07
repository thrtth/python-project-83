"""init

Revision ID: 6cbf532203f5
Revises:
Create Date: 2024-07-10 15:22:12.709202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '6cbf532203f5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('url_checks',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('url_id', sa.Integer(), nullable=True),
                    sa.Column('status_code', sa.Integer(), nullable=True),
                    sa.Column('h1', sa.Text(), nullable=True),
                    sa.Column('title', sa.Text(), nullable=True),
                    sa.Column('description', sa.Text(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['url_id'], ['urls.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('url_checks')
    op.drop_table('urls')
    # ### end Alembic commands ###
