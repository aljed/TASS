#! /usr/bin/env python3

from pathlib import Path

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'


AGGREGATED_AIRPORT_REVIEWS_DATA_PATH: Path = Path("../data/aggregated_airport_reviews.csv")
AIRPORT_IDS_DATA_PATH: Path = Path("../data/eu_airports_df.csv")
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

    airport_ids: pd.DataFrame = pd.read_csv(AIRPORT_IDS_DATA_PATH)
    airport_ids = airport_ids.drop_duplicates(subset="iata_code")
    airport_ids["cleaned_airport_name"] = airport_ids["name"].map(clean_string)
    airport_ids = airport_ids.drop_duplicates(subset="cleaned_airport_name")

    aggregated_airport_reviews["cleaned_airport_name"] = aggregated_airport_reviews["name"].map(clean_string)
    aggregated_airport_reviews = aggregated_airport_reviews.drop_duplicates(subset="cleaned_airport_name")

    merged_airport_reviews: pd.DataFrame = pd.merge(airport_ids, aggregated_airport_reviews, on="cleaned_airport_name")

    merged_airport_reviews["name_x"] = merged_airport_reviews["name_x"].values
    merged_airport_reviews = merged_airport_reviews.drop(["name_y", "cleaned_airport_name",
                                                          "ident", "type", "iso_country", "coordinates"], axis=1)
    merged_airport_reviews = merged_airport_reviews.rename(columns={"iata_code": "id", "name_x": "name"})
    merged_airport_reviews = swap_columns(merged_airport_reviews, "id", "name")
    merged_airport_reviews.to_csv(MERGED_AIRPORT_REVIEWS_SAVE_PATH, index=False)
