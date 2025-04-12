
import pandas as pd

def clean_data():
    df = pd.read_csv('data/raw_historical_draws.csv')
    df.dropna(inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df.to_csv('data/clean_historical_draws.csv', index=False)

clean_data()
