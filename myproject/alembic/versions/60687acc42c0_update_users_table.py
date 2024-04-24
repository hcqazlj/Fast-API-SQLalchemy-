"""update users table

Revision ID: 60687acc42c0
Revises: 62e695750dc7
Create Date: 2024-03-26 20:10:31.737136

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60687acc42c0'
down_revision: Union[str, None] = '62e695750dc7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('basicsetting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('setting_type', sa.String(length=50), nullable=True),
    sa.Column('setting_content', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_basicsetting_id'), 'basicsetting', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_basicsetting_id'), table_name='basicsetting')
    op.drop_table('basicsetting')
    # ### end Alembic commands ###
