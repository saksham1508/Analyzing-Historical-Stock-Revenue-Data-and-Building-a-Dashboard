"""
Script to extract Tesla and GameStop stock and revenue data and save as xlsx in data/ folder.
"""
import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def extract_tesla_stock():
    tsla = yf.Ticker("TSLA")
    tesla_data = tsla.history(period="max")
    tesla_data.reset_index(inplace=True)
    return tesla_data

def extract_tesla_revenue():
    url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table_rows = soup.find_all('tr')
    data = []
    for row in table_rows:
        cols = row.find_all('td')
        if cols:
            date = cols[0].text.strip()
            revenue_str = cols[1].text.strip().replace('$', '').replace(',', '')
            try:
                revenue = int(revenue_str)
            except ValueError:
                continue
            data.append({'Date': date, 'Revenue': revenue})
    tesla_revenue = pd.DataFrame(data)
    tesla_revenue.dropna(inplace=True)
    tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]
    return tesla_revenue

def extract_gme_stock():
    gme = yf.Ticker("GME")
    gme_data = gme.history(period="5y")
    gme_data.reset_index(inplace=True)
    return gme_data

def extract_gme_revenue():
    url = "https://www.macrotrends.net/stocks/charts/GME/gme/revenue"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table_rows = soup.find_all('tr')
    data = []
    for row in table_rows:
        cols = row.find_all('td')
        if cols:
            date = cols[0].text.strip()
            revenue_str = cols[1].text.strip().replace('$', '').replace(',', '')
            try:
                revenue = int(revenue_str)
            except ValueError:
                continue
            data.append({'Date': date, 'Revenue': revenue})
    gme_revenue = pd.DataFrame(data)
    gme_revenue.dropna(inplace=True)
    gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]
    return gme_revenue

def save_to_xlsx(df, filename):
    os.makedirs('data', exist_ok=True)
    df.to_excel(os.path.join('data', filename), index=False)

def main():
    save_to_xlsx(extract_tesla_stock(), 'tesla_stock.xlsx')
    save_to_xlsx(extract_tesla_revenue(), 'tesla_revenue.xlsx')
    save_to_xlsx(extract_gme_stock(), 'gme_stock.xlsx')
    save_to_xlsx(extract_gme_revenue(), 'gme_revenue.xlsx')

if __name__ == "__main__":
    main()
