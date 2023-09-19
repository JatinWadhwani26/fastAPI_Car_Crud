"""empty message

Revision ID: 314273ad95aa
Revises: ef6a267bbb71
Create Date: 2023-09-19 15:51:08.962523

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '314273ad95aa'
down_revision: Union[str, None] = 'ef6a267bbb71'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('car_image', 'image_size',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=50),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('car_image', 'image_size',
               existing_type=sa.String(length=50),
               type_=mysql.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
