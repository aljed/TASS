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
    projected_airport_reviews: pd.DataFrame = airport_reviews_raw.drop(
        ["link", "title", "author", "author_country", "date",
         "content", "experience_airport", "date_visit", "type_traveller",
         "terminal_seating_rating","terminal_signs_rating","food_beverages_rating",
         "wifi_connectivity_rating","airport_staff_rating","recommended"],
        axis=1)
    renamed_airport_reviews: pd.DataFrame = projected_airport_reviews.rename(columns={
        "airport_name": "name",
        "queuing_rating": "queuing_efficiency",
        "terminal_cleanliness_rating": "cleanliness",
        "airport_shopping_rating": "shopping_facilities"
    })
    aggregated_airport_reviews: pd.DataFrame = renamed_airport_reviews.groupby("name").mean()
    airport_reviews_final: pd.DataFrame = aggregated_airport_reviews[
        ~aggregated_airport_reviews["overall_rating"].isna()]
    columns_to_fill_empty_values_in = [
    # columns_to_fill_empty_values_in: list[str] = [
        "queuing_efficiency", "cleanliness", "shopping_facilities"]
    for column in columns_to_fill_empty_values_in:
        airport_reviews_final[column] = airport_reviews_final[column].fillna(
            airport_reviews_final["overall_rating"])
        
    airport_reviews_final.to_csv(AGGREGATED_AIRPORT_REVIEWS_SAVE_PATH)
