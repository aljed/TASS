from typing import Any

import pandas as pd
import networkx as nx

import server

def test_construct_graph() -> None:
    flights_data: list[list] = [
        ["Airport A", "Airport B", "Airline 1", 100.],
        ["Airport A", "Airport B", "Airline 2", 100.],
        ["Airport B", "Airport C", "Airline 1", 200.],
        ["Airport A", "Airport C", "Airline 1", 250.]
    ]
    flights: pd.DataFrame = pd.DataFrame(
        flights_data, columns=["departure_airport_id", "destination_airport_id", "airline_id", "distance"])
    airline_opinion_data: server.OpinionData = {
        "Airline 1": {
            "overall_rating": 1.
        },
        "Airline 2": {
            "overall_rating": 10.
        }
    }
    airport_opinion_data: server.OpinionData = {
        "Airport A": {
            "overall_rating": 10.
        },
        "Airport B": {
            "overall_rating": 10.
        },
        "Airport C": {
            "overall_rating": 10.
        }
    }
    rating_weights: dict[str, Any] = {
        "distance": 1.,
        "overall_airline": 1.,
        "overall_airport": 1.,
    }

    G: nx.DiGraph = server.construct_graph(flights, airline_opinion_data, airport_opinion_data, rating_weights)

    assert G.number_of_nodes() == 3
    assert G.number_of_edges() == 3
    assert G["Airport A"]["Airport B"]["airline_id"] == "Airline 2"
    assert G["Airport B"]["Airport C"]["airline_id"] == "Airline 1"
    assert G["Airport A"]["Airport C"]["airline_id"] == "Airline 1"
