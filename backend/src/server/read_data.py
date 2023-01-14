import pandas as pd
from pathlib import Path

OpinionData = dict[str, dict[str, float]]

def read_opinion_data(path_to_opinion_file: str) -> OpinionData:
    df: pd.DataFrame = pd.read_csv(path_to_opinion_file)
    all_opinion_data: OpinionData = {}
    for row in df.itertuples():
        single_opinion_data: dict[str, float] = row._asdict()
        single_opinion_data.pop("Index")
        single_opinion_data.pop("id")
        all_opinion_data[row.id] = single_opinion_data

    return all_opinion_data

if __name__ == "__main__":
    data_path: Path = Path("mock_data")
    print(read_opinion_data(data_path / "airlines.csv"))
    print(read_opinion_data(data_path / "airlines.csv"))
    flights = pd.read_csv(data_path / "airlines.csv")
    print(flights.head())
