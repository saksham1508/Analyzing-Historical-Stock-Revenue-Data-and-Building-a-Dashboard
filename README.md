
# Analyzing Historical Stock & Revenue Data and Building a Dashboard

This project demonstrates how to extract, clean, analyze, and visualize historical stock and revenue data for companies such as Tesla and GameStop. It includes data extraction from Yahoo Finance and MacroTrends, data cleaning, analysis, and an interactive dashboard.

## Project Structure


```text
├── src/                # Source code modules
│   ├── data_loader.py
│   ├── data_cleaner.py
│   ├── data_analysis.py
│   ├── visualization.py
│   ├── dashboard.py
│   ├── extract_data.py
│   └── main.py
├── data/               # Extracted data (xlsx files)
├── notebooks/          # Jupyter notebooks
├── outputs/            # Generated plots/outputs
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Features

- Extract stock data using yfinance
- Extract revenue data using web scraping (BeautifulSoup)
- Clean and preprocess data
- Analyze trends in stock and revenue
- Visualize data with Matplotlib and Plotly
- Interactive dashboard with Streamlit

## Setup Instructions


1. **Clone the repository:**



```sh
git clone <repo-url>
cd Analyzing-Historical-Stock-Revenue-Data-and-Building-a-Dashboard
```

2. **Install dependencies:**



```sh
pip install -r requirements.txt
```

3. **Extract data:**



```sh
python src/extract_data.py
```
This will save the extracted data as `.xlsx` files in the `data/` folder.

4. **Run the main analysis script:**



```sh
python src/main.py
```

5. **Launch the dashboard:**



```sh
streamlit run src/dashboard.py
```

## Data Sources

- [Yahoo Finance](https://finance.yahoo.com/)
- [MacroTrends](https://www.macrotrends.net/)

## Folder Descriptions

- `src/`: All source code modules
- `data/`: Saved data files (after extraction)
- `notebooks/`: Jupyter notebooks for exploration
- `outputs/`: Generated plots and results

## License

This project is for educational purposes.

