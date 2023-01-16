#! /usr/bin/env python3

##############################################
##  Mikołaj Pańka                           ##
##  TASS projekt 2                          ##
##                                          ##
##  Styczeń 2023                            ##
##############################################


import pandas as pd


CONTINENT_COUNTRY_PATH  = "../data/continent_country.tsv"
COUNTRY_CODES_PATH      = "../data/countries.dat"

DO_LOG = True


def main():
    continent_country = pd.read_csv(CONTINENT_COUNTRY_PATH, sep=" \t", engine="python")
    # eu_countries = eu_countries[eu_countries["Continent"] == "Europe"]
    # eu_countries_list = eu_countries["Country"].to_list()
    # if DO_LOG:
        # print(continent_country)

    country_codes = pd.read_csv(COUNTRY_CODES_PATH, names=["name", "iso", "continent"])
    for i in range(len(country_codes)):
        n = country_codes.loc[i, "name"]
        c = continent_country[1][continent_country["Country"] == n]
        print(c)
        # country_codes.loc[i, "continent"] = continent_country.loc[continent_country["Country"] == country_codes.loc[i, "name"], "Continent"]
    
    
    # eu_iso = country_codes["iso"][country_codes["name"].isin(eu_countries_list)]
    
    
    
    # country_codes_list = country_codes["iso"].to_list()
    # if DO_LOG:
    #     print(eu_iso)
    # eu_iso["name"] = 
    

if __name__ == "__main__":
    main()
