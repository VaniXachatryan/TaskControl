"""init tables

Revision ID: f46a7b8a9a5f
Revises: 
Create Date: 2024-02-09 22:45:08.516237

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f46a7b8a9a5f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('batches',
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_table('brigades',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lines',
    sa.Column('code', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shifts',
    sa.Column('start_at', sa.DateTime(), nullable=False),
    sa.Column('end_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('work_centers',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('line_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('is_closed', sa.Boolean(), nullable=False),
    sa.Column('closed_at', sa.DateTime(), nullable=True),
    sa.Column('work_center_id', sa.Integer(), nullable=False),
    sa.Column('shift_id', sa.Integer(), nullable=False),
    sa.Column('brigade_id', sa.Integer(), nullable=False),
    sa.Column('batch_id', sa.Integer(), nullable=False),
    sa.Column('nomenclature', sa.String(), nullable=False),
    sa.Column('ekn_code', sa.String(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['batch_id'], ['batches.id'], ),
    sa.ForeignKeyConstraint(['brigade_id'], ['brigades.id'], ),
    sa.ForeignKeyConstraint(['line_id'], ['lines.id'], ),
    sa.ForeignKeyConstraint(['shift_id'], ['shifts.id'], ),
    sa.ForeignKeyConstraint(['work_center_id'], ['work_centers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tasks')
    op.drop_table('work_centers')
    op.drop_table('shifts')
    op.drop_table('lines')
    op.drop_table('brigades')
    op.drop_table('batches')
    # ### end Alembic commands ###