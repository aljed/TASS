#! /usr/bin/env python3

##########################################################
##  Aleksander Jedynak, Piotr Satała, Mikołaj Pańka     ##
##  TASS projekt 2                                      ##
##                                                      ##
##  Styczeń 2023                                        ##
##########################################################


import re
import pandas as pd


AIRPORT_CODES_PATH  = "../data/airport-codes_csv.csv"
AIRPORT_TYPES       = ["medium_airport", "large_airport"]
BAD_DF_PATH         = "../data/bad_names_df.csv"
COLUMNS             = ["ident", "type", "name", "iso_country", "iata_code", "coordinates"]  # coordinates: lon, lat
DROP_DUPLICATE_COLS = ["name", "iata_code", "coordinates"]
GOOD_DF_PATH        = "../data/good_names_df.csv"

DO_LOG = True


def read_airports(path: str) -> pd.DataFrame:
    if DO_LOG:
        print("Reading airport data from: " + path)
    df = pd.read_csv(path)
    if DO_LOG:
        print("Selecting medium and large airports from Europe...")
    df = df[df["continent"] == "EU"]
    df = df[df["type"].isin(AIRPORT_TYPES)]
    if DO_LOG:
        print(f"Selecting columns: {COLUMNS}.")
    df = df[COLUMNS]

    return df


# remove missing or repeating data
def rm_missing(df: pd.DataFrame) -> pd.DataFrame:
    n = len(df)
    if DO_LOG:
        print(f"Total rows: {len(df)}")
        print("Dropping missing and repeating values:")
    df.dropna(inplace=True)  # some iata codes repeat but not in EU
    if DO_LOG:
        print(f"Dropped {n - len(df)} rows.")
    nn = len(df)
    for col in DROP_DUPLICATE_COLS:
        df.drop_duplicates(subset=[col], inplace=True)
    if DO_LOG:
        print(f"Dropped {nn - len(df)} rows.")

    return df


def contains_any(str, set):
    return 1 in [c in str for c in set]


# some airport names in csv have messed-up characters
def is_alphanum(df: pd.DataFrame, col: str) -> list:
    ret = []
    for nm in df[col].to_list():
        if re.sub(r"[\s+.'-/\",]", "", nm, flags=re.UNICODE).isalnum() \
        & ~contains_any(nm, "Ã¼Å½"):
            ret.append(True)
        else:
            ret.append(False)

    return ret


def is_not_alphanum(df: pd.DataFrame, col: str) -> list:
    ret = []
    for nm in df[col].to_list():
        if re.sub(r"[\s+.'-/\",]", "", nm, flags=re.UNICODE).isalnum() \
        & ~contains_any(nm, "Ã¼Å½"):
            ret.append(False)
        else:
            ret.append(True)

    return ret


def extract_bad_names(df: pd.DataFrame) -> pd.DataFrame:
    if DO_LOG:
        print("Extracting airports with messed-up UTF-8 names:")
    good_names_idx = is_alphanum(df, "name")
    bad_names_idx = is_not_alphanum(df, "name")
    good_df = df.loc[good_names_idx]
    good_df.to_csv(GOOD_DF_PATH, index=None)
    bad_df = df.loc[bad_names_idx]
    bad_df.to_csv(BAD_DF_PATH, index=None)
    if DO_LOG:
        print(f"... {len(good_df)} good names, {len(bad_df)} messed-up names")
        print("... saved files: " + GOOD_DF_PATH + ", " + BAD_DF_PATH)

    return bad_df


def main():
    df = read_airports(AIRPORT_CODES_PATH)    
    rm_missing(df)
    if DO_LOG:
        print(df)
        print(df.shape)
    extract_bad_names(df)
    #
    # Now go and correct the messed-up names in the CSV by hand.
    #


if __name__ == "__main__":
    main()
    if DO_LOG:
        print("###   Now go and correct the messed-up names in the CSV by hand.   ###")
