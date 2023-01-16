#! /usr/bin/env python3

##########################################################
##  Aleksander Jedynak, Piotr Satała, Mikołaj Pańka     ##
##  TASS projekt 2                                      ##
##                                                      ##
##  Styczeń 2023                                        ##
##########################################################


import os
import pandas as pd


CORRECTED_DF_PATH   = "../data/corrected_df.csv"
GOOD_DF_PATH        = "../data/good_names_df.csv"
BAD_DF_PATH         = "../data/bad_names_df.csv"
EU_AIRPORTS_PATH    = "../data/eu_airports_df.csv"

CLEAN = True


def main():
    good_df = pd.read_csv(GOOD_DF_PATH)
    corrected_df = pd.read_csv(CORRECTED_DF_PATH)
    merged_df = pd.concat([good_df, corrected_df])
    merged_df.sort_values(by="ident", inplace=True)
    merged_df.to_csv(EU_AIRPORTS_PATH, index=None)
    if CLEAN:
        os.remove(GOOD_DF_PATH)
        os.remove(BAD_DF_PATH)


if __name__ == "__main__":
    main()
