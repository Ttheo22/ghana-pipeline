import requests
import json
from config.indicators import BASE_URL, COUNTRY_CODE, GHANA_INDICATORS, START_YEAR, END_YEAR

def fetch_indicator(indicator_code):
    url = f"{BASE_URL}/country/{COUNTRY_CODE}/indicator/{indicator_code}" #url path for the worldBank indicator built dynamically instead of hard coding
    params = {
        "format": "json",
        "per_page": 100,
        "date": f"{START_YEAR}:{END_YEAR}"
    }
    try:
        response  = requests.get(url, params=params, timeout=30)
        response.raise_for_status()  # Raise an error for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {indicator_code}: {e}")
        return None

def fetch_all():
    all_data = {}
    for code in GHANA_INDICATORS:
        print(f"Fetching {code}...")
        result = fetch_indicator(code)
        if result is not None:
            all_data[code] = result 
    return all_data