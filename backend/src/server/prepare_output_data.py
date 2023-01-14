from typing import Any

import networkx as nx

def prepare_output_data(G: nx.DiGraph, shortest_paths: list[list[str]]) -> list[dict[str, Any]]:
    return [__get_connection_info(G, path) for path in shortest_paths]

def __get_connection_info(G: nx.DiGraph, path: list[str]) -> dict[str, Any]:
    distance: float = nx.path_weight(G, path, "weight")
    transfer_airport_ids: list[str] = path[1:-1]
    airline_ids: list[str] = []
    for i in range(len(path) - 1):
        departure_airport_id: str = path[i]
        destination_airport_id: str = path[i + 1]
        airline_ids.append(G[departure_airport_id][destination_airport_id]["airline_id"])
    return {
        "distance": distance,
        "transfer_airport_ids": transfer_airport_ids,
        "airline_ids": airline_ids
    }