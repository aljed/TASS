# TASS

## Kolejność postępowania

1. `scripts/extract_bad_names.py`
2. Ręczne poprawki nazw lkotnisk, lub skopiopwać z `corrected_df.csv`
3. `scripts/merge_good_bad.py`
4. `scripts/make_flights.py`
5. `scripts/prep_airlines.py`

## Przygotowanie danych

### `scripts/extract_bad_names.py`

1. Wczytuje dane z oryginalnego CSV.
2. Ekstrahuje średnie i duże lotniska z Europy.
3. Usuwa rekordy z brakujacymi danymi.
4. Usuwa duplikaty - sprawdza wg kolumny `iata_code`. W EU nie ma duplikatów. Są w USA kody IATA powtarzające się w EU.
5. Niektóre nazwy lotnisk mają nieprawidłowe znaki w nazwach. Rozdziela dane na dwa DataFrame'y: jeden z nieprawidłowymi nazwami, drugi z pozostałymi.
6. Zapisuje DF'y na dysk.

### `scripts/merge_good_bad.py`

1. Wczytuje dane z dwóch CSV: ten z prawidłowymi nazwami i ten z poprawionymi.
2. Scala dwa DF'y w jednego.
3. Sortuje wg kolumny `ident`.
4. Zapisuje na dysk jako gotowe dane.

### Ręczne poprawki

Poprawki wykonuje się po wykonaniu skryptu `extract_bad_names.py`, a przed wykonaniem `merge_good_bad.py`.
W tej wersji jest 157 wpisów z nazwami lotnisk zawierającymi nieprawidłowe znaki.
Poprawia się je ręcznie otwierając CSV w Excelu i wyszukując po kodach IATA prawidłowe nazwy lotnisk w Internecie.
**Konieczne** jest zapisanie poprawionego pliku jako `corrected_df.csv`.
Skrypt łączący `merge_good_bad.py` **usuwa** pliki z nieprawidłowymi i dobrymi nazwami lotnisk, a poprawiony ręcznie pozostawia nietkniętym.

Plik `data/corrected.csv` zawiera poprawione nazwy.

### `scripts/make_flights.py`

Tworzy tabelę lotów w Europie z danych w `routes.dat` i `eu_airports_df.csv`. Oblicza dystans w kilometrach.
**TO DO:** poprawić airline_id na wygodną dla człowieka.
Kolumny:

