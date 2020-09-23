from dataclasses import dataclass
from app import db

@dataclass
class Product(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))
    price = db.Column(db.Float)

    product_name: str
    price: float 
