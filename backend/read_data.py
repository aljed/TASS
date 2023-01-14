import pandas as pd

DATA_PATH: str = "mock_data/"

def read_opinion_data(path_to_opinion_file: str) -> dict[str, dict[str, float]]:
    df: pd.DataFrame = pd.read_csv(path_to_opinion_file)
    all_opinion_data: dict[str, dict[str, float]] = {}
    for row in df.itertuples():
        single_opinion_data: dict[str, float] = row._asdict()
        single_opinion_data.pop("Index")
        single_opinion_data.pop("id")
        all_opinion_data[row.id] = single_opinion_data

    return all_opinion_data

if __name__ == "__main__":
    print(read_opinion_data(f"{DATA_PATH}airlines.csv"))
    print(read_opinion_data(f"{DATA_PATH}airports.csv"))
    flights = pd.read_csv(f"{DATA_PATH}flights.csv")
    print(flights.head())
