import pandas as pd
from src.db import get_connection

def load_inventory():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM inventory", conn)
    conn.close()
    return df

def load_hospitals():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM hospitals", conn)
    conn.close()
    return df
