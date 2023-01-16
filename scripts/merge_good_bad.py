#! /usr/bin/env python3

##############################################
##  Mikołaj Pańka                           ##
##  TASS projekt 2                          ##
##                                          ##
##  Styczeń 2023                            ##
##############################################


import pandas as pd


CORRECTED_DF_PATH   = "../data/corrected_df.csv"
GOOD_DF_PATH        = "../data/good_names_df.csv"
EU_AIRPORTS_PATH    = "../data/eu_aiports_df.csv"


def main():
    good_df = pd.read_csv(GOOD_DF_PATH)
    corrected_df = pd.read_csv(CORRECTED_DF_PATH)
    merged_df = pd.concat([good_df, corrected_df])
    merged_df.sort_values(by="ident", inplace=True)
    merged_df.to_csv(EU_AIRPORTS_PATH, index=None)


if __name__ == "__main__":
    main()
