"""Seed feedback_data table

Revision ID: 206af614ad78
Revises: f66558563671
Create Date: 2024-10-13 19:45:30.076117

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '206af614ad78'
down_revision: Union[str, None] = 'f66558563671'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Insert sample data with created_at
    op.execute("""
        INSERT INTO feedback_data (product_name, customer_feedback, sentiment, created_at) 
        VALUES 
        ('Product A', 'The product is great but could be improved', 'neutral', CURRENT_TIMESTAMP),
        ('Product B', 'Amazing experience, loved it!', 'positive', CURRENT_TIMESTAMP),
        ('Product C', 'The quality was bad, disappointed', 'negative', CURRENT_TIMESTAMP);
    """)

def downgrade():
    # Optionally, delete the seed data if necessary during downgrade
    op.execute("""
        DELETE FROM feedback_data
        WHERE product_name IN ('Product A', 'Product B', 'Product C');
    """)
