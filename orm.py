from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy import create_engine, ForeignKey, CheckConstraint
from utilities import SingleInstanceClass


Base = declarative_base()


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


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    full_name = Column(String)
    country = Column(String)
    nip = Column(String(10))
    zip_code = Column(String(5))
    city = Column(String)
    address = Column(String)


class Supplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    full_name = Column(String)
    country = Column(String)
    nip = Column(String(10))
    zip_code = Column(String(5))
    city = Column(String)
    address = Column(String)


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


# DataBase manager


class DBManager:

    def __init__(self):
        dal = DataAccessLayer()
        dal.conn_string = r"sqlite:///my_db.db"
        dal.echo = True
        dal.connect()
        self.session = dal.session_maker()

    def get_companies_names(self):
        return self.session.query(Supplier.name).all()



db_manager = DBManager()
