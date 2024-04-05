from sqlalchemy import Column, Integer, Float, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    type = Column(Enum('Type1', 'Type2', 'Type3'), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Float, nullable=False)
