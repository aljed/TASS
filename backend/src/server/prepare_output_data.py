from typing import Union

import networkx as nx

from .data_reader import OpinionData

OutputData = list[dict[str, Union[str, float]]]


def prepare_output_data(
        G: nx.DiGraph,
        shortest_paths: list[list[str]],
        airline_id_to_name_map: dict[str, str],
        airport_id_to_name_map: dict[str, str],
        include_ratings_in_output: bool,
        airline_opinion_data: OpinionData,
        airport_opinion_data: OpinionData) -> OutputData:
    return [__get_connection_info(
            G,
            path,
            airline_id_to_name_map,
            airport_id_to_name_map,
            include_ratings_in_output,
            airline_opinion_data,
            airport_opinion_data) for path in shortest_paths]


def __get_connection_info(
        G: nx.DiGraph,
        path: list[str],
        airline_id_to_name_map: dict[str, str],
        airport_id_to_name_map: dict[str, str],
        include_ratings_in_output: bool,
        airline_opinion_data: OpinionData,
        airport_opinion_data: OpinionData) -> dict:

    distance: float = nx.path_weight(G, path, "weight")
    transfer_airports: list[dict] = __get_transfer_airports(
        path, airport_id_to_name_map, include_ratings_in_output, airport_opinion_data)
    airlines: list[dict] = __get_airlines(
        G, path, airline_id_to_name_map, include_ratings_in_output, airline_opinion_data)

    return {
        "distance": distance,
        "transfer_airports": transfer_airports,
        "airlines": airlines
    }


def __get_transfer_airports(
        path: list[str],
        airport_id_to_name_map: dict[str, str],
        include_ratings_in_output: bool,
        airport_opinion_data: OpinionData) -> list[dict]:

    transfer_airport_ids: list[str] = path[1:-1]
    transfer_airports: list[dict] = []
    for transfer_airport_id in transfer_airport_ids:
        transfer_airport = {
            "id": transfer_airport_id,
            "name": airport_id_to_name_map[transfer_airport_id]
        }
        if include_ratings_in_output:
            transfer_airport["ratings"] = airport_opinion_data[transfer_airport_id]
        transfer_airports.append(transfer_airport)
    return transfer_airports


def __get_airlines(
        G: nx.DiGraph,
        path: list[str],
        airline_id_to_name_map: dict[str, str],
        include_ratings_in_output: bool,
        airline_opinion_data: OpinionData) -> list[dict]:

    airline_ids: list[str] = []
    for i in range(len(path) - 1):
        departure_airport_id: str = path[i]
        destination_airport_id: str = path[i + 1]
        airline_ids.append(G[departure_airport_id][destination_airport_id]["airline_id"])

    airlines: list[dict] = []
    for airline_id in airline_ids:
        airline = {
            "id": airline_id,
            "name": airline_id_to_name_map[airline_id]
        }
        if include_ratings_in_output:
            airline["ratings"] = airline_opinion_data[airline_id]
        airlines.append(airline)
    return airlines
