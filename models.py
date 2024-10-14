from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class FeedbackData(Base):
    __tablename__ = 'feedback_data'
    id = Column(Integer, primary_key=True)
    product_name = Column(String(50), nullable=False)
    customer_feedback = Column(Text, nullable=False)
    sentiment = Column(String(20), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)

# Create a MetaData object
metadata = Base.metadata
