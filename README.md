# TASS

## Kolejność postępowania

W celu przygotowania danych, przed uruchomieniem wyszukiwarki należy ręcznie wykonać skrypty w następującej kolejności:

1. `scripts/extract_bad_names.py`
2. `scripts/merge_good_bad.py`
3. `scripts/prep_airlines.py`
4. `scripts/make_flights.py`
5. 

## Przygotowanie danych

Dane o liniach lotniczy, lotniskach, siatce połączeń i opiniach pasażerów zostały pozyskane z otwartych źródeł.
Przygotowano skrypty przekształcające te dane do postaci użytecznej dla wyszukiwarki.
Skrypty oczyszczają dane z brakujących lub niepoprawnych wpisów, weryfikują spójność.
Pliki wykorzystywane przez wyszukiwarkę często są wynikiem przekształcenia więcej niż jednego pliku wejściowego.

### `extract_bad_names.py`

Wejście:
 - `airport-codes_csv.csv`

Wyjście:
 - `bad_names_df.csv`
 - `good_names_df.csv`

Działanie:
1. Wczytuje dane z oryginalnego CSV.
2. Ekstrahuje średnie i duże lotniska z Europy.
3. Usuwa rekordy z brakujacymi danymi.
4. Usuwa duplikaty - sprawdza wg kolumny `iata_code`. W EU nie ma duplikatów. Są w USA kody IATA powtarzające się w EU.
5. Niektóre nazwy lotnisk mają nieprawidłowe znaki w nazwach. Rozdziela dane na dwa DataFrame'y: jeden z nieprawidłowymi nazwami, drugi z pozostałymi.
6. Zapisuje DF'y na dysk.

### `merge_good_bad.py`

Wejście:
 - `good_names_df.csv`
 - `corrected_df.csv`

Wyjście:
 - `eu_airports_df.csv`

Inne:
 - `bad_names_df.csv`

Działanie:
1. Wczytuje dane z dwóch CSV: ten z prawidłowymi nazwami i ten z poprawionymi.
2. Scala dwa DF'y w jednego.
3. Sortuje wg kolumny `ident`.
4. Zapisuje na dysk jako gotowe dane.
5. Usuwa pliki `good_names_df.csv` i `bad_names_df.csv` z dysku.
6. Nie usuwa `corrected_df.csv`.

### Ręczne poprawki

Plik `corrected_df.csv` zawiera już poprawione nazwy. Jeśli nie ma tego pliku,
to poprawki wykonuje się po wykonaniu skryptu `extract_bad_names.py`,
a przed wykonaniem `merge_good_bad.py`. W tej wersji jest 157 wpisów z nazwami lotnisk
zawierającymi nieprawidłowe znaki. Poprawia się je ręcznie otwierając
`bad_names_df.csv` w Excelu i wyszukując po kodach IATA prawidłowe nazwy lotnisk w Internecie.
**Konieczne** jest zapisanie poprawionego pliku jako `corrected_df.csv`.

### `prep_airlines.py`

Wejście:
 - `continent_country.tsv`
 - `countries.dat`
 - `airlines.dat`
 - `eu_flights.csv`

Wyjście:
 - `eu_country_iso.csv`
 - `eu_airlines_iata.csv`

Działanie:

1. Przygotowuje tabelę europejskich krajów wraz ich kodami ISO.
2. Przygotowuje tabelę europejskich linii lotniczych wraz z ich kodami IATA.
3. 

### `make_flights.py`

Tworzy tabelę lotów w Europie z danych w `routes.dat` i `eu_airports_df.csv`. Oblicza dystans w kilometrach.
**TO DO:** Usunąć loty pomiędzy rosyjskimi lotniskami na terenie Azji -- Rosja jest oznaczona jako Europa.
Kolumny:
 - departure_airport_id
 - destination_airport_id
 - airline_id
 - distance



