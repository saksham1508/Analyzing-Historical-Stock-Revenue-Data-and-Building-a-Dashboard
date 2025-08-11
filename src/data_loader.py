"""
Functions to load stock and revenue data from CSV or other sources.
"""
import pandas as pd

def load_stock_data(filepath):
    """Load stock data from a CSV file."""
    return pd.read_csv(filepath)

def load_revenue_data(filepath):
    """Load revenue data from a CSV file."""
    return pd.read_csv(filepath)
