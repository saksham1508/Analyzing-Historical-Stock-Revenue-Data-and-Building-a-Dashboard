"""
Main script to run the analysis pipeline.
"""

import pandas as pd
from src.data_loader import load_stock_data, load_revenue_data
from src.data_cleaner import clean_stock_data, clean_revenue_data
from src.data_analysis import analyze_stock_trends, analyze_revenue_trends
from src.visualization import plot_stock_data, plot_revenue_data


def main():
    stock_path = 'data/tesla_stock.xlsx'  # Update with actual path
    revenue_path = 'data/tesla_revenue.xlsx'  # Update with actual path
    stock_df = clean_stock_data(pd.read_excel(stock_path))
    revenue_df = clean_revenue_data(pd.read_excel(revenue_path))
    print('Stock Data Analysis:')
    print(analyze_stock_trends(stock_df))
    print('Revenue Data Analysis:')
    print(analyze_revenue_trends(revenue_df))
    plot_stock_data(stock_df)
    plot_revenue_data(revenue_df)

if __name__ == '__main__':
    main()
