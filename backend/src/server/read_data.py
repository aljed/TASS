import pandas as pd
from pathlib import Path
from typing import Union

OpinionData = dict[str, dict[str, float]]
StaticData = tuple[OpinionData, OpinionData, pd.DataFrame]

class DataReader:
    
    def __init__(self) -> None:
        self.__data_path: Union[Path, None] = None
    
    def set_data_path(self, value) -> None:
        self.__data_path = value

    def __call__(self) -> StaticData:
        if self.__data_path is None:
            raise Exception("Data path was not initialized")
        airline_opinion_data: OpinionData = self.__read_opinion_data(self.__data_path / "airlines.csv")
        airport_opinion_data: OpinionData = self.__read_opinion_data(self.__data_path / "airports.csv")
        flights: pd.DataFrame = pd.read_csv(self.__data_path / "flights.csv")
        return airline_opinion_data, airport_opinion_data, flights

    def __read_opinion_data(self, path_to_opinion_file: str) -> OpinionData:
        df: pd.DataFrame = pd.read_csv(path_to_opinion_file)
        all_opinion_data: OpinionData = {}
        for row in df.itertuples():
            single_opinion_data: dict[str, float] = row._asdict()
            single_opinion_data.pop("Index")
            single_opinion_data.pop("id")
            all_opinion_data[row.id] = single_opinion_data

        return all_opinion_data
