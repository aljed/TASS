#! /usr/bin/env python3

##########################################################
##  Aleksander Jedynak, Piotr Satała, Mikołaj Pańka     ##
##  TASS projekt 2                                      ##
##                                                      ##
##  Styczeń 2023                                        ##
##########################################################

#
# Create eu_flights.csv with columns:
# departure_airport_id | destination_airport_id | airline_id | distance
# 


from math import acos, sin, cos, radians, floor
import pandas as pd


FLIGHTS_CSV_PATH        = "../data/eu_flights.csv"
ROUTES_PATH             = "../data/routes.dat"
GLOBAL_ROUTES_COLUMNS   = ["airline", "airline_id", "source_airport", "source_airport_id", "destination_airport", "destination_airport_id", "codeshare", "stops", "equipment"]
ROUTES_COLUMNS          = ["airline", "source_airport", "destination_airport", "stops"]
NEW_COLUMNS             = ["departure_airport_id", "destination_airport_id", "airline_id", "distance"]
EU_AIRPORTS_PATH        = "../data/eu_airports_df.csv"

DO_LOG = True


def load_routes(path: str) -> pd.DataFrame:
    if DO_LOG:
        print("Reading global route data from: " + path)
    df = pd.read_csv(ROUTES_PATH, names=GLOBAL_ROUTES_COLUMNS)[ROUTES_COLUMNS]
    n = len(df)
    if DO_LOG:
        print(df)
        print("Dropping missing and repeating values:")
    df.dropna(inplace=True)
    if DO_LOG:
        print(f"Dropped {n - len(df)} rows.")
    nn = len(df)
    df.drop_duplicates(inplace=True)
    if DO_LOG:
        print(f"Dropped {nn - len(df)} rows.")

    return df


def get_eu_routes(global_routes: pd.DataFrame, eu_ap: pd.DataFrame) -> pd.DataFrame:
#
# TODO:
# remove routes within russian asian teritory
# because country of Russia is marked as european
#
    eu_ap_list = eu_ap["iata_code"].unique().tolist()
    eu_routes = global_routes[global_routes["source_airport"].isin(eu_ap_list) & global_routes["destination_airport"].isin(eu_ap_list)]
    if DO_LOG:
        print(f"Extracted {len(eu_routes)} EU routes.")
    return eu_routes


def swap_columns(df: pd.DataFrame, col1, col2) -> pd.DataFrame:
    col_list = list(df.columns)
    x, y = col_list.index(col1), col_list.index(col2)
    col_list[y], col_list[x] = col_list[x], col_list[y]
    df = df[col_list]
    return df


def calc_distances(routes, airports: pd.DataFrame):
# Spherical Law of Cosines.
# d = acos( sin φ1 ⋅ sin φ2 + cos φ1 ⋅ cos φ2 ⋅ cos Δλ ) ⋅ R
    R = 6371
    n = len(routes)
    for i in range(len(routes)):
        if DO_LOG & (i%1000 == 0):
            print(f"{i} of {n}")
        dep_coords = airports[airports["iata_code"] == routes.loc[i, "departure_airport_id"]]["coordinates"]
        dep_coords_str = dep_coords.to_list()[0]
        lon1 = dep_coords_str.split()[0][:-1]  # a ',' at end of longitude
        lon1 = radians(float(lon1))
        lat1 = dep_coords_str.split()[1]
        lat1 = radians(float(lat1))
        
        dest_coords = airports[airports["iata_code"] == routes.loc[i, "destination_airport_id"]]["coordinates"]
        dest_coords_str = dest_coords.to_list()[0]
        lon2 = dest_coords_str.split()[0][:-1]  # a ',' at end of longitude
        lon2 = radians(float(lon2))
        lat2 = dest_coords_str.split()[1]
        lat2 = radians(float(lat2))
        
        dlon = lon1 - lon2  # order irrelevant - cos is even
        
        routes.loc[i, "distance"] = floor(acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(dlon)) * R)        


def main():
    global_routes_df = load_routes(ROUTES_PATH)
    if DO_LOG:
        print("Reading EU airport data from: " + EU_AIRPORTS_PATH)
    eu_airports = pd.read_csv(EU_AIRPORTS_PATH)
    eu_routes = get_eu_routes(global_routes_df, eu_airports)
    n = len(eu_routes)
    if DO_LOG:
        print(eu_routes)
# There is single flight that has one stop-over.
# There is no info as to which airport is the stop-over.
# Remove it to keep data clean.
        print("Removing routes with stop-overs.")    
    eu_routes = eu_routes[eu_routes["stops"] == 0].reset_index(drop=True)
    if DO_LOG:
        print(f"Dropped {n - len(eu_routes)} rows.")
        print(f"Rearranging columns.")
    eu_routes = swap_columns(eu_routes, "airline", "destination_airport")
    eu_routes = swap_columns(eu_routes, "destination_airport", "source_airport")
    eu_routes.columns = NEW_COLUMNS
    if DO_LOG:
        print("Calculating flight distances.")
    calc_distances(eu_routes, eu_airports)
    eu_routes.to_csv(FLIGHTS_CSV_PATH)
    if DO_LOG:
        print("Saved EU flight routes to " + FLIGHTS_CSV_PATH)
        print(eu_routes)


if __name__ == "__main__":
    main()
