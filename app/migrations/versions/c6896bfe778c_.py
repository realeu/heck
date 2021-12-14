"""empty message

Revision ID: c6896bfe778c
Revises: 1a9671324408
Create Date: 2019-06-28 18:16:59.782609

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "c6896bfe778c"
down_revision = "1a9671324408"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("channels", sa.Column("restrict_users", sa.Boolean(), nullable=True))
    op.add_column("channels", sa.Column("name", sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("channels", "restrict_users")
    op.drop_column("channels", "name")
    # ### end Alembic commands ###
