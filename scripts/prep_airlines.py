#! /usr/bin/env python3

##########################################################
##  Aleksander Jedynak, Piotr Satała, Mikołaj Pańka     ##
##  TASS projekt 2                                      ##
##                                                      ##
##  Styczeń 2023                                        ##
##########################################################


import pandas as pd


CONTINENT_COUNTRY_PATH  = "../data/continent_country.tsv"
COUNTRY_CODES_PATH      = "../data/countries.dat"
EU_COUNTRY_ISO_CODES    = "../data/eu_country_iso.csv"

DO_LOG = True


def make_airports_iso():
    eu_countries = pd.read_csv(CONTINENT_COUNTRY_PATH, sep=" \t", engine="python")
    eu_countries = eu_countries[eu_countries["Continent"] == "Europe"]
    eu_countries_list = eu_countries["Country"].to_list()
    if DO_LOG:
        print(eu_countries)
    country_codes = pd.read_csv(COUNTRY_CODES_PATH, names=["name", "iso", "continent"])
    
    for i in range(len(country_codes)):
        n = country_codes.loc[i, "name"]
        if n in eu_countries_list:
            country_codes.loc[i, "continent"] = "europe"
    country_codes = country_codes[country_codes["continent"] == "europe"]
    
    return country_codes[["name", "iso"]]


def main():
    eu_ap_iso = make_airports_iso()
    if DO_LOG:
        print(eu_ap_iso)
        print("Saving EU country ISO codes to " + EU_COUNTRY_ISO_CODES)
    eu_ap_iso.to_csv(EU_COUNTRY_ISO_CODES, index=None)


if __name__ == "__main__":
    main()
