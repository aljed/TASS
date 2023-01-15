# TASS

## Scripts

`scripts/extract_bad_names.py`
1. Wczytuje dane z oryginalnego CSV.
2. Ekstrahuje średnie i duże lotniska z Europy
3. Usuwa rekordy z brakujacymi danymi
4. Usuwa duplikaty - sprawdza wg kolumny `iata_code`. W EU nie ma duplikatów. Są w USA kody IATA powtarzające się w EU.
5. Niektóre nazwy lotnisk mają nieprawidłowe znaki w nazwach. Rozdziela dane na dwa DataFrame'y: jeden z nieprawidłowymi nazwami, drugi z pozostałymi.
6. Zapisuje DF'y na dysk.

