"""
Functions to generate plots and charts for stock and revenue data.
"""
import matplotlib.pyplot as plt


import os

def plot_stock_data(df, name="stock"):
    """Plot stock data and save to outputs/ folder."""
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Close'])
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    os.makedirs('outputs', exist_ok=True)
    plt.savefig(f"outputs/{name}_stock_plot.png")
    plt.show()


def plot_revenue_data(df, name="revenue"):
    """Plot revenue data and save to outputs/ folder."""
    plt.figure(figsize=(10,5))
    plt.plot(df['Date'], df['Revenue'])
    plt.title('Revenue Over Time')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    os.makedirs('outputs', exist_ok=True)
    plt.savefig(f"outputs/{name}_revenue_plot.png")
    plt.show()
