#! /usr/bin/env python3

from pathlib import Path

import pandas as pd

UNCLEANED_FLIGHTS_PATH: Path = Path("../data/eu_flights.csv")
CLEANED_FLIGHTS_PATH: Path = Path("../final_data/flights.csv")
AIRPORTS_PATH: Path = Path("../final_data/airports.csv")
AIRLINES_PATH: Path = Path("../final_data/airlines.csv")

# UNCLEANED_FLIGHTS_PATH: Path = Path("data/eu_flights.csv")
# CLEANED_FLIGHTS_PATH: Path = Path("final_data/flights.csv")
# AIRPORTS_PATH: Path = Path("final_data/airports.csv")
# AIRLINES_PATH: Path = Path("final_data/airports.csv")

if __name__ == "__main__":
    airports: pd.DataFrame = pd.read_csv(AIRPORTS_PATH)
    airlines: pd.DataFrame = pd.read_csv(AIRLINES_PATH)
    uncleaned_flights: pd.DataFrame = pd.read_csv(UNCLEANED_FLIGHTS_PATH)

    uncleaned_flights = uncleaned_flights.loc[uncleaned_flights['destination_airport_id'].isin(airports["id"].values)]
    uncleaned_flights = uncleaned_flights.loc[uncleaned_flights['departure_airport_id'].isin(airports["id"].values)]
    cleaned_flights = uncleaned_flights.loc[uncleaned_flights['airline_id'].isin(airlines["id"].values)]

    cleaned_flights.to_csv(CLEANED_FLIGHTS_PATH, index=False)
