from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    describtion = Column(TEXT)
    img = Column(String)
    price = Column(REAL)
    release_date = Column(String)
    company = Column(String)
    discount = Column(REAL)
    available = Column(BOOLEAN)


class Admin(Base):
    __tablename__ = 'admins'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class Cart(Base):
    __tablename__ = 'cart'
    id = Column(Integer, primary_key=True)
    productID = Column(Integer)



