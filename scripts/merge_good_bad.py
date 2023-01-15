#! /usr/bin/env python3

##############################################
##  Mikołaj Pańka                           ##
##  TASS projekt 2                          ##
##                                          ##
##  Styczeń 2023                            ##
##############################################


import pandas as pd


# AIRPORT_CODES_PATH  = "../data/airport-codes_csv.csv"
# AIRPORT_TYPES       = ["medium_airport", "large_airport"]
# BAD_DF_PATH         = "../data/bad_df.csv"
BETTER_DF_PATH      = "../data/better_df.csv"
# COLUMNS             = ["ident", "type", "name", "iata_code", "coordinates"]  # coordinates: lon, lat
GOOD_DF_PATH        = "../data/good_df.csv"
MERGED_DF_PATH      = "../data/merged_df.csv"

VERBOSE = True


def main():
    good_df = pd.read_csv(GOOD_DF_PATH)
    better_df = pd.read_csv(BETTER_DF_PATH)
    merged_df = pd.concat([good_df, better_df])
    merged_df.sort_values(by="ident", inplace=True)
    merged_df.to_csv(MERGED_DF_PATH, index=None)


if __name__ == "__main__":
    main()
