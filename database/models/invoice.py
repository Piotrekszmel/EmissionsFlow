from sqlalchemy import Column, Integer, Float, String

from database.models.base import Base


class Invoice(Base):
    __tablename__ = 'invoices'
    
    id = Column(Integer, primary_key=True)
    nip = Column(String(length=12), nullable=False)
    seller_name = Column(String, nullable=False)
    seller_address = Column(String, nullable=False)
    seller_tax_id = Column(String, nullable=False)
    buyer_name = Column(String, nullable=False)
    buyer_address = Column(String, nullable=False)
    buyer_tax_id = Column(String, nullable=False)
    invoice_number = Column(String, nullable=False)
    invoice_issue_date = Column(String, nullable=False)
    product_description = Column(String, nullable=False)
    product_measure = Column(String, nullable=False)
    product_quantity = Column(Float, nullable=False)
    unit_price_excluding_tax = Column(Float, nullable=False)
    value_excluding_tax = Column(Float, nullable=False)
    tax_rates = Column(String, nullable=False)
    total_net_sales_value = Column(Float, nullable=False)
    tax_amounts = Column(Float, nullable=False)
    total_amount_including_tax = Column(Float, nullable=False)
