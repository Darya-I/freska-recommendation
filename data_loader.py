# data_loader.py

import pandas as pd
from models import session, UserCartItem, UserPreference, UserSession

def load_user_cart_items():
    query = session.query(UserCartItem).statement
    return pd.read_sql(query, session.bind)

def load_user_preferences():
    query = session.query(UserPreference).statement
    return pd.read_sql(query, session.bind)

def load_user_sessions():
    query = session.query(UserSession).statement
    return pd.read_sql(query, session.bind)
