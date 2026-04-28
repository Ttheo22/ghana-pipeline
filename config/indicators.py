COUNTRY_CODE = "GH"
START_YEAR = 2000
END_YEAR = 2023
BASE_URL = "https://api.worldbank.org"

GHANA_INDICATORS = {
    "NY.GDP.MKTP.KD.ZG":{
        "name": "gdp_growth_rate",
        "label": "GDP Growth Rate",
        "unit": "Annual %",
        "category": "growth",
    },
    "PA.NUS.FCRF": {
        "name": "exchange_rate_usd",
        "label": "Exchange Rate (GHS per USD)",
        "unit": "LCU per US$",
        "category": "monetary",
    },
}