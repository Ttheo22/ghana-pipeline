import os
import pandas as pd

def load(df):
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/ghana_indicators.csv', index=False)
    print("Data saved to data/processed/ghana_indicators.csv")