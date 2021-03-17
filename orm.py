from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, Float, Date, Boolean
from sqlalchemy import ForeignKey, UniqueConstraint, create_engine, join
from math import fsum

from utilities import SingleInstanceClass

Base = declarative_base()


class AbstractReqMethods:
    """
    Class provide basics methods which are required by AbstractTableModels from models with they are connected
    """

    @staticmethod
    def cols():
        """
        :return:  list of cols_names(str)"""
        return []

    @staticmethod
    def get_editable_keys():
        """
        :return:  list of int which represents index of string from self.cols() which are editable in AbstractModels"""
        return []

    def _values(self):
        """
        :return: List of values for each column available under self.cols()
        """
        return []

    def __getitem__(self, item):
        return self._values()[item]

    def __setitem__(self, key, value):
        if key in self.get_editable_keys():
            setattr(self, self.cols()[key], value)
            self.price = value


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


class Product(Base, AbstractReqMethods):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    category = Column(String, ForeignKey('categories.name'))
    active = Column(Boolean, default=True)

    __table_args__ = (UniqueConstraint(name, category, name='name_category'),)

    @staticmethod
    def cols():
        return ['name', 'category', 'status']

    def _values(self):
        return [self.name, self.category,  'active' if self.active else 'inactive']


class Category(Base):
    __tablename__ = 'categories'

    name = Column(String, primary_key=True, autoincrement=False)


class PriceTable(Base, AbstractReqMethods):
    __tablename__ = 'price_tables'

    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), primary_key=True)
    price = Column(Float)
    active = Column(Boolean, default=True)

    product = relationship('Product', lazy='joined')

    @staticmethod
    def cols():
        return ['product_name', 'price', 'category', 'status']

    @staticmethod
    def get_editable_keys():
        return [PriceTable.cols().index('price')]

    def _values(self):
        return [self.product.name, self.price, self.product.category, 'active' if self.active else 'inactive']


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    order_date = Column(Date)
    delivery_date = Column(Date)
    # todo maybe add new Bool column "Delivered"


class OrderDetail(Base, AbstractReqMethods):
    __tablename__ = 'orders_details'

    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = Column(Integer)
    unit_price = Column(Float)
    total_price = column_property(quantity * unit_price)

    product = relationship('Product', lazy='joined')

    @staticmethod
    def cols():
        return ['product_name', 'category', 'quantity', 'unit_price', 'total_price']

    def _values(self):
        return [self.product.name, self.product.category, self.quantity, self.unit_price, self.total_price]


class Country(Base):
    __tablename__ = 'countries'

    name = Column(String)
    code = Column(String(2), primary_key=True)


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


orders_join = join(Order.__table__, Customer.__table__, Order.customer_id == Customer.id)


class CustomerOrder(Base, AbstractReqMethods):
    __table__ = orders_join

    customer_id = column_property(Order.customer_id, Customer.id)

    @staticmethod
    def cols():
        return ['customer_name', 'order_date', 'delivery_date']

    def _values(self):
        return [self.name, self.order_date, self.delivery_date]
