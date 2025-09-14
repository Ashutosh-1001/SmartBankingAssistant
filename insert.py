# src/inserting_data.py
import json
from sqlalchemy import create_engine, Table, Column, String, Integer, Float, MetaData, Date
from sqlalchemy.dialects.mysql import VARCHAR, DOUBLE
from sqlalchemy.exc import IntegrityError
import os
from datetime import datetime

DB_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:root@localhost:3306/bankllm")

engine = create_engine(DB_URL, echo=False)
meta = MetaData()

customer_table = Table(
    'customer_profile', meta,
    Column('CustomerID', String(80), primary_key=True),
    Column('FirstName', String(80)),
    Column('LastName', String(80)),
    Column('Gender', String(10)),
    Column('Email', String(120)),
    Column('Phone', String(40)),
    Column('Age', Integer),
    Column('City', String(80)),
    Column('Country', String(80)),
    Column('CurrentBalance', Double),
    Column('Currency', String(10)),
    Column('TotalTransactions', Integer),
    Column('TotalDeposits', Double),
    Column('TotalWithdrawals', Double),
    Column('AverageTransactionAmount', Double),
    Column('TotalCashback', Double),
    Column('LastTransactionDate', String(20)),
    Column('PreferredContactMethod', String(20)),
    Column('AverageMonthlySpending', Double),
    Column('HighestTransactionAmount', Double),
    Column('LowestTransactionAmount', Double),
    Column('TotalNumberOfAccounts', Integer),
    Column('AccountStatus', String(20)),
    Column('RiskProfile', String(20)),
    Column('DepositStatus', String(10)),
    Column('CreatedAt', String(30))
)

product_table = Table(
    'products', meta,
    Column('ProductID', Integer, primary_key=True),
    Column('ProductName', String(150)),
    Column('Category', String(80)),
    Column('InterestRate', Double),
    Column('EligibilityCriteria', String(200)),
    Column('RiskLevel', String(20)),
    Column('Description', String(500))
)

def create_tables():
    meta.create_all(engine)
    print("Tables created (if not exists).")

def insert_json(customers_file="customers.json", products_file="products.json"):
    with open(customers_file) as f:
        customers = json.load(f)
    with open(products_file) as f:
        products = json.load(f)

    conn = engine.connect()
    for c in customers:
        try:
            conn.execute(customer_table.insert().values(**c))
        except IntegrityError:
            pass
    for p in products:
        try:
            conn.execute(product_table.insert().values(**p))
        except IntegrityError:
            pass
    conn.close()
    print("Inserted data into DB.")

if __name__ == "__main__":
    create_tables()
    insert_json()
