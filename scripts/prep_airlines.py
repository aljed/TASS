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
AIRLINES_DAT_PATH       = "../data/airlines.dat"
EU_AIRLINES_IATA        = "../data/eu_airlines_iata.csv"
COLUMNS                 = ["name", "iata"]


DO_LOG = True


def make_airlines_iata(eu_countries_list):
    airlines_df = pd.read_csv(AIRLINES_DAT_PATH, \
        names=["airline_id", "name", "alias", "iata", "icao", "callsign", "country", "active"], \
        na_values=["\\N", "-"], keep_default_na=True )
    print(airlines_df)
    print(eu_countries_list)
    airlines_df = airlines_df[airlines_df["country"].isin(eu_countries_list)]
    airlines_df = airlines_df[COLUMNS].reset_index(drop=True)
    airlines_df.dropna(inplace=True)
    # airlines_df = airlines_df[COLUMNS]
    return airlines_df


def make_airports_iso():
    eu_countries = pd.read_csv(CONTINENT_COUNTRY_PATH, sep=" \t", engine="python")
    eu_countries = eu_countries[eu_countries["Continent"] == "Europe"]
    eu_countries_list = eu_countries["Country"].to_list()
    eu_countries_list.extend(["Kazakhstan", "Russia", "Russian Federation", "Turkey"])
    if DO_LOG:
        print(eu_countries)
    country_codes = pd.read_csv(COUNTRY_CODES_PATH, names=["name", "iso", "continent"])
    
    for i in range(len(country_codes)):
        n = country_codes.loc[i, "name"]
        if n in eu_countries_list:
            country_codes.loc[i, "continent"] = "europe"
    country_codes = country_codes[country_codes["continent"] == "europe"]
    
    return eu_countries_list, country_codes[["name", "iso"]]


def main():
    if DO_LOG:
        print("Associating EU countries with their ISO codes.")
    eu_countries_list, eu_ap_iso = make_airports_iso()
    if DO_LOG:
        print(eu_ap_iso)
        print("Saving EU country ISO codes to " + EU_COUNTRY_ISO_CODES)
    eu_ap_iso.to_csv(EU_COUNTRY_ISO_CODES, index=None)
    if DO_LOG:
        print("Associating airlines with their IATA codes.")
    airlines_iata_df = make_airlines_iata(eu_countries_list)
    if DO_LOG:
        print("Saving EU airlines IATA codes to " + EU_AIRLINES_IATA)
    airlines_iata_df.to_csv(EU_AIRLINES_IATA, index=None, columns=COLUMNS)
    if DO_LOG:
        print(airlines_iata_df)


if __name__ == "__main__":
    main()
