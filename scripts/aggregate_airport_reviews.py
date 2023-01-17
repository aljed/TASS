#! /usr/bin/env python3

from pathlib import Path

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

AIRPORT_REVIEWS_RAW_DATA_PATH: Path = Path("../data/airport_reviews.csv")
AGGREGATED_AIRPORT_REVIEWS_SAVE_PATH: Path = Path("../data/aggregated_airport_reviews.csv")
# AIRPORT_REVIEWS_RAW_DATA_PATH: Path = Path("../data/airport_reviews.csv")
# AGGREGATED_AIRPORT_REVIEWS_SAVE_PATH: Path = Path("../data/aggregated_airport_reviews.csv")

if __name__ == "__main__":
    airport_reviews_raw: pd.DataFrame = pd.read_csv(
        AIRPORT_REVIEWS_RAW_DATA_PATH)
    