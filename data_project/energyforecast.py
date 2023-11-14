# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/modules/00_energyforecast.ipynb.

# %% auto 0
__all__ = ['aemo_price_demand']

# %% ../nbs/modules/00_energyforecast.ipynb 2
from nbdev.showdoc import *
import polars as pl
import matplotlib.pyplot as plt
import pandas as pd

import requests
import csv
from io import StringIO
from datetime import datetime

# %% ../nbs/modules/00_energyforecast.ipynb 3
def aemo_price_demand(state: str, year: int, month: int):
    assert isinstance(month, int) and isinstance(year, int)
    assert (
        year >= 1998 and year <= datetime.now().year
    ), "Year must be from 1998 to current year"
    assert month >= 1 and month <= 12, "Month between 1 to 12"

    if month < 10:
        month_str = f"0{month}"
    else:
        month_str = str(month)

    state = state.lower()

    # TODO: closest match / fuzzy match
    state_code_map = {"vic": "VIC1", "nsw": "NSW1"}

    state_code = state_code_map[state]
    try:
        url = f"https://aemo.com.au/aemo/data/nem/priceanddemand/PRICE_AND_DEMAND_{year}{month_str}_{state_code}.csv"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)

        response.raise_for_status()  # Check for any errors in the response
        csv_content = StringIO(response.text)
    except:
        pass

    return pd.read_csv(csv_content, parse_dates=True)
