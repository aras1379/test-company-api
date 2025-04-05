from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from sqlalchemy.orm import relationship
from app.database import Base 

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")
    
class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    products = relationship("Product", back_populates="category")
    
class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product")
    stock = Column(Integer)
    
class Pricing(Base):
    __tablename__ = "pricing"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    product = relationship("Product")
    
    price = Column(Float)
    currency_id = Column(Integer, ForeignKey("currency.id"))
    currency = relationship("Currency")
    
    
class Currency(Base):
    __tablename__ = "currency"
    
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String)
    