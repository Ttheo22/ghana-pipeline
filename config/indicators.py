COUNTRY_CODE = "GH"
START_YEAR = 2000
END_YEAR = 2025
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
    "FP.CPI.TOTL.ZG": {
        "name": "inflation_rate",
        "label": "Inflation Rate",
        "unit": "Annual %",
        "category": "monetary",
    },
    "GC.XPN.TOTL.GD.ZS": {
        "name": "govt_debt_pct-gdp",
        "label": "Government Debt )",
        "unit": "% of GDP",
        "category": "fiscal",
    },
    "SL.UEM.TOTL.ZS": {
        "name": "unemployment_rate",
        "label": "Unemployment Rate",
        "unit": "Percent of total labor force",
        "category": "labor",
    },

}