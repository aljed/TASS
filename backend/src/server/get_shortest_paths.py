from itertools import islice

import networkx as nx


def get_shortest_paths(
        G: nx.DiGraph, departure_airport_id: str, destination_airport_id: str, n_shortest_paths: int) -> list[list[str]]:
    return list(islice(
        nx.shortest_simple_paths(G, departure_airport_id, destination_airport_id, weight="weight"),
        n_shortest_paths))
