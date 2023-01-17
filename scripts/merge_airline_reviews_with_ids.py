#! /usr/bin/env python3

from pathlib import Path

import pandas as pd

AGGREGATED_AIRLINE_REVIEWS_DATA_PATH: Path = Path("../data/aggregated_airline_reviews.csv")
AIRLINE_IDS_DATA_PATH: Path = Path("../data/eu_airlines_iata.csv")
MERGED_AIRLINE_REVIEWS_SAVE_PATH: Path = Path("../final_data/airlines.csv")
# AGGREGATED_AIRLINE_REVIEWS_DATA_PATH: Path = Path("data/aggregated_airline_reviews.csv")
# AIRLINE_IDS_DATA_PATH: Path = Path("data/eu_airlines_iata.csv")
# MERGED_AIRLINE_REVIEWS_SAVE_PATH: Path = Path("final_data/airlines.csv")

def clean_string(string: str) -> str:
    return (''.join(c for c in string if c.isalnum())).lower()

def swap_columns(df, column1, column2):
    i = list(df.columns)
    a, b = i.index(column1), i.index(column2)
    i[b], i[a] = i[a], i[b]
    df = df[i]
    return df

if __name__ == "__main__":
    aggregated_airline_reviews: pd.DataFrame = pd.read_csv(
        AGGREGATED_AIRLINE_REVIEWS_DATA_PATH)
    airline_ids: pd.DataFrame = pd.read_csv(AIRLINE_IDS_DATA_PATH)

    airline_ids = airline_ids.drop_duplicates(subset="iata")
    airline_ids["cleaned_airline_name"] = airline_ids["name"].map(clean_string)
    airline_ids = airline_ids.drop_duplicates(subset="cleaned_airline_name")

    aggregated_airline_reviews["cleaned_airline_name"] = aggregated_airline_reviews["airline_name"].map(clean_string)
    aggregated_airline_reviews = aggregated_airline_reviews.drop_duplicates(subset="cleaned_airline_name")

    merged_airline_reviews: pd.DataFrame = pd.merge(airline_ids, aggregated_airline_reviews, on="cleaned_airline_name")
    print(merged_airline_reviews.columns)
    merged_airline_reviews = merged_airline_reviews.drop(["airline_name", "cleaned_airline_name"], axis=1)
    merged_airline_reviews = merged_airline_reviews.rename(columns={"iata": "id"})
    merged_airline_reviews = swap_columns(merged_airline_reviews, "id", "name")
    merged_airline_reviews.to_csv(MERGED_AIRLINE_REVIEWS_SAVE_PATH, index=False)
