from typing import Any

import networkx as nx
import pandas as pd

from .read_data import OpinionData
from .calculate_weight import calculate_weight


def construct_graph(
        flights: pd.DataFrame,
        airline_opinion_data: OpinionData,
        airport_opinion_data: OpinionData,
        rating_weights: dict[str, Any]) -> nx.DiGraph:

    G = nx.DiGraph()
    for row in flights.itertuples():
        weight: float = calculate_weight(
            row.airline_id,
            row.destination_airport_id,
            row.distance,
            airline_opinion_data,
            airport_opinion_data,
            rating_weights)
        G.add_node(row.departure_airport_id)
        G.add_node(row.destination_airport_id)
        if __should_add_current_edge(G, row.departure_airport_id, row.destination_airport_id, weight):
            G.add_edge(row.departure_airport_id, row.destination_airport_id, weight=weight, airline_id=row.airline_id)
    return G


def __should_add_current_edge(
        G: nx.DiGraph,
        departure_airport_id: str,
        destination_airport_id: str,
        new_weight: float) -> bool:
    if not G.has_edge(departure_airport_id, destination_airport_id):
        return True
    return G[departure_airport_id][destination_airport_id]["weight"] > new_weight
