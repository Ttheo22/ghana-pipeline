from src.extract import fetch_all
from src.transform import transform
from src.load import load
from src.visualise import plot_inflation, plot_all_indicators

if __name__ == "__main__":
    raw_data = fetch_all()
    transformed_data = transform(raw_data)
    load(transformed_data)
    plot_inflation()    
    plot_all_indicators()