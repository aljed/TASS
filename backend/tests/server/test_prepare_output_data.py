from typing import Any

import networkx as nx

import server


def test_prepare_output_data() -> None:
    G: nx.DiGraph = nx.DiGraph()
    G.add_nodes_from(["A", "B", "C"])
    G.add_edge("A", "B", weight=100., airline_id="Airline 1")
    G.add_edge("B", "C", weight=200., airline_id="Airline 2")
    G.add_edge("A", "C", weight=350., airline_id="Airline 1")
    shortest_paths: list[list[str]] = [
        ["A", "B", "C"],
        ["A", "C"]
    ]

    output_data: list[dict[str, Any]] = server.prepare_output_data(G, shortest_paths)

    assert output_data == [
        {
            "distance": 300.0,
            "transfer_airport_ids": [
                "B"
            ],
            "airline_ids": [
                "Airline 1",
                "Airline 2"
            ]
        },
        {
            "distance": 350.0,
            "transfer_airport_ids": [],
            "airline_ids": [
                "Airline 1"
            ]
        }
    ]
