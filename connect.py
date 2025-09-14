
from sqlalchemy import create_engine, text
import os
import pandas as pd

DB_URL = os.getenv("DATABASE_URL", "mysql+pymysql://root:root@localhost:3306/bankllm")
engine = create_engine(DB_URL, echo=False)

def get_customer(customer_id):
    q = text("SELECT * FROM customer_profile WHERE CustomerID = :cid")
    with engine.connect() as conn:
        res = conn.execute(q, {"cid": customer_id}).mappings().fetchone()
    return dict(res) if res else None

def get_all_products():
    q = text("SELECT * FROM products")
    with engine.connect() as conn:
        res = conn.execute(q).mappings().all()
    return [dict(r) for r in res]
