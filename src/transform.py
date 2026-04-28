import pandas as pd
from config.indicators import GHANA_INDICATORS

def transform(raw_data):
    rows = []
    for code, result in raw_data.items():
        records = result[1]
        for record in records:
            if record in records:
                if record['value'] is None:
                    continue
                rows.append({
                    'year': int(record['date']),
                    'indicator_code': code,
                    'indicator_name': GHANA_INDICATORS[code]['name'],
                    'category': GHANA_INDICATORS[code]['category'],
                    'value': record['value']

                    })
    df = pd.DataFrame(rows)
    return df