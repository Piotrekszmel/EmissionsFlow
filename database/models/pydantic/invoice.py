from typing import Optional
from pydantic import BaseModel, field_validator, constr

class Invoice(BaseModel):
    id: Optional[int] = None
    nip: str = str[constr(min_length=10, max_length=12)]
    seller_name: str
    seller_address: str
    seller_tax_id: str
    buyer_name: str
    buyer_address: str
    buyer_tax_id: str
    invoice_number: str
    invoice_issue_date: str
    product_description: str
    product_measure: str
    product_quantity: float
    unit_price_excluding_tax: float
    value_excluding_tax: float
    tax_rates: str
    total_net_sales_value: float
    tax_amounts: float
    total_amount_including_tax: float
