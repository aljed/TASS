#! /usr/bin/env python3

from pathlib import Path

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


AGGREGATED_AIRPORT_REVIEWS_DATA_PATH: Path = Path("../data/aggregated_airport_reviews.csv")
AIRPORT_IDS_DATA_PATH: Path = Path("../data/eu_airports_iata.csv")
MERGED_AIRPORT_REVIEWS_SAVE_PATH: Path = Path("../final_data/airports.csv")
# AGGREGATED_AIRPORT_REVIEWS_DATA_PATH: Path = Path("data/aggregated_airport_reviews.csv")
# AIRPORT_IDS_DATA_PATH: Path = Path("data/eu_airports_iata.csv")
# MERGED_AIRPORT_REVIEWS_SAVE_PATH: Path = Path("final_data/airports.csv")


def clean_string(string: str) -> str:
    return (''.join(c for c in string if c.isalnum())).lower()


def swap_columns(df, column1, column2):
    i = list(df.columns)
    a, b = i.index(column1), i.index(column2)
    i[b], i[a] = i[a], i[b]
    df = df[i]
    return df


if __name__ == "__main__":
    aggregated_airport_reviews: pd.DataFrame = pd.read_csv(
        AGGREGATED_AIRPORT_REVIEWS_DATA_PATH)
