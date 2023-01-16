from pathlib import Path

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

AIRLINE_REVIEWS_RAW_DATA_PATH: Path = Path("data/airline_reviews.csv")
AGGREGATED_AIRLINE_REVIEWS_SAVE_PATH: Path = Path("data/aggregated_airline_reviews.csv")

if __name__ == "__main__":
    airline_reviews_raw: pd.DataFrame = pd.read_csv(
        AIRLINE_REVIEWS_RAW_DATA_PATH)
    projected_airline_reviews: pd.DataFrame = airline_reviews_raw.drop(
        ["link", "title", "author", "author", "author_country", "date",
         "content", "aircraft", "type_traveller", "cabin_flown", "route",
         "ground_service_rating", "wifi_connectivity_rating", "recommended"],
        axis=1)
    renamed_airline_reviews: pd.DataFrame = projected_airline_reviews.rename(columns={
        "seat_comfort_rating": "seat_comfort",
        "cabin_staff_rating": "service_quality",
        "food_beverages_rating": "food_quality",
        "inflight_entertainment_rating": "onboard_entertainment",
        "value_money_rating": "quality_price_ratio"
    })
    aggregated_airline_reviews: pd.DataFrame = renamed_airline_reviews.groupby("airline_name").mean()
    airline_reviews_final: pd.DataFrame = aggregated_airline_reviews[
        ~aggregated_airline_reviews["overall_rating"].isna()]
    
    columns_to_fill_empty_values_in: list[str] = [
        "seat_comfort", "service_quality", "food_quality", "onboard_entertainment", "quality_price_ratio"]
    for column in columns_to_fill_empty_values_in:
        airline_reviews_final[column] = airline_reviews_final[column].fillna(
            airline_reviews_final["overall_rating"])

    airline_reviews_final.to_csv(AGGREGATED_AIRLINE_REVIEWS_SAVE_PATH)
    
