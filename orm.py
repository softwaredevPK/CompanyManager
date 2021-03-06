from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property, sessionmaker
from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from sqlalchemy import ForeignKey, UniqueConstraint, create_engine

from utilities import SingleInstanceClass

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    full_name = Column(String, unique=True)
    country = Column(String, ForeignKey('countries.name'))
    tin_code = Column(String)
    zip_code = Column(String)
    city = Column(String)
    address = Column(String)
    email = Column(String)
    phone_number = Column(Integer)
    is_person = Column(Boolean)
    country_tin = column_property(country + tin_code)

    __table_args__ = (UniqueConstraint(country, tin_code, name='country_tin'),)


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    full_name = Column(String)
    country = Column(String, ForeignKey('countries.name'))
    tin_code = Column(String)
    zip_code = Column(String(5))
    city = Column(String)
    address = Column(String)
    email = Column(String)
    phone_number = Column(Integer)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'))
    name = Column(String)


class PriceTable(Base):
    __tablename__ = 'price_tables'

    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), primary_key=True)
    price = Column(Float)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(Date)
    delivery_date = Column(Date)


class OrderDetail(Base):
    __tablename__ = 'orders_details'

    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)


class Country(Base):
    __tablename__ = 'countries'

    name = Column(String)
    code = Column(String(2), primary_key=True)

# todo SIngleTOn to rethink - rebuild
class DataAccessLayer(SingleInstanceClass):
    """Class to manage access to DB"""

    def __init__(self):
        self.conn_string = None
        self.echo = None
        self.engine = None
        self.session_maker = None
        self.session = None

    def connect(self):
        self.engine = create_engine(self.conn_string, echo=self.echo)
        Base.metadata.create_all(self.engine)
        self.session_maker = sessionmaker(bind=self.engine)
