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

        airline_opinion_data: OpinionData
        airline_id_to_name_map: dict[str, str]
        airline_opinion_data, airline_id_to_name_map = self.__read_opinion_data(self.__data_path / "airlines.csv")

        airport_opinion_data: OpinionData
        airport_id_to_name_map: dict[str, str]
        airport_opinion_data, airport_id_to_name_map = self.__read_opinion_data(self.__data_path / "airports.csv")

        flights: pd.DataFrame = pd.read_csv(self.__data_path / "flights.csv")

        return (
            airline_opinion_data,
            airline_id_to_name_map,
            airport_opinion_data,
            airport_id_to_name_map,
            flights)

    def __read_opinion_data(self, path_to_opinion_file: str) -> tuple[OpinionData, dict[str, str]]:
        df: pd.DataFrame = pd.read_csv(path_to_opinion_file)
        all_opinion_data: OpinionData = {}
        id_to_name_map: dict[str, str] = {}
        for row in df.itertuples():
            single_opinion_data: dict[str, float] = row._asdict()
            single_opinion_data.pop("Index")
            single_opinion_data.pop("id")
            single_opinion_data.pop("name")
            all_opinion_data[row.id] = single_opinion_data
            id_to_name_map[row.id] = row.name

        return all_opinion_data, id_to_name_map
