"""
Optional: Launch a dashboard using Streamlit.
"""
import streamlit as st
import pandas as pd
from src.data_loader import load_stock_data, load_revenue_data
from src.data_cleaner import clean_stock_data, clean_revenue_data
from src.visualization import plot_stock_data, plot_revenue_data

st.title('Stock and Revenue Dashboard')

stock_file = st.file_uploader('Upload Stock Data CSV')
revenue_file = st.file_uploader('Upload Revenue Data CSV')

if stock_file and revenue_file:
    stock_df = clean_stock_data(load_stock_data(stock_file))
    revenue_df = clean_revenue_data(load_revenue_data(revenue_file))
    st.subheader('Stock Data')
    st.write(stock_df.head())
    plot_stock_data(stock_df)
    st.subheader('Revenue Data')
    st.write(revenue_df.head())
    plot_revenue_data(revenue_df)
