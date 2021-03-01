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
    tin_code = Column(String)
    zip_code = Column(String)
    city = Column(String)
    address = Column(String)
    email = Column(String)
    phone_number = Column(Integer)


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


class Country(Base):
    __tablename__ = 'countries'

    name = Column(String)
    code = Column(String(2), primary_key=True)


# DataBase manager


class DBManager:

    def __init__(self):
        dal = DataAccessLayer()
        dal.conn_string = r"sqlite:///my_db.db"
        dal.echo = True
        dal.connect()
        self.engine = dal.engine
        self.session = dal.session_maker()

    def get_companies_names(self):
        return [i[0] for i in self.session.query(Supplier.name).all()]

    def get_countries_names(self):
        return [i[0] for i in self.session.query(Country.name).all()]

    def get_country_code(self, country):
        return self.session.query(Country.code).filter(Country.name == country).one()[0]


db_manager = DBManager()


if __name__ == '__main__':
    #  use to populate DB with countries
    import pandas as pd
    from pathlib import Path

    df = pd.read_csv(Path().absolute().joinpath('Countries_table.csv'))
    df = df[~pd.isna(df['Alpha-2 code'])]
    df['Country'] = df['Country'].str.replace('\(.*\)', '').str.replace('\[.*\]', '').str.strip()
    items = []
    for _, row in df.iterrows():
        items.append(Country(name=row['Country'], code=row['Alpha-2 code']))
    db_manager.session.add_all(items)
    db_manager.session.commit()