import networkx as nx

import server


def test_prepare_output_data() -> None:
    G: nx.DiGraph = nx.DiGraph()
    G.add_nodes_from(["A", "B", "C"])
    G.add_edge("A", "B", weight=100., airline_id="1")
    G.add_edge("B", "C", weight=200., airline_id="2")
    G.add_edge("A", "C", weight=350., airline_id="1")
    shortest_paths: list[list[str]] = [
        ["A", "B", "C"],
        ["A", "C"]
    ]
    airline_id_to_name_map: dict[str, str] = {
        "1": "Airline 1",
        "2": "Airline 2"
    }
    airport_id_to_name_map: dict[str, str] = {
        "A": "Airport A",
        "B": "Airport B",
        "C": "Airport C"
    }

    output_data: server.OutputData = server.prepare_output_data(
        G,
        shortest_paths,
        airline_id_to_name_map,
        airport_id_to_name_map,
        include_ratings_in_output=False,
        airline_opinion_data=None,
        airport_opinion_data=None)

    assert output_data == [
        {
            "distance": 300.0,
            "transfer_airports": [
                {
                    "id": "B",
                    "name": "Airport B"
                }
            ],
            "airlines": [
                {
                    "id": "1",
                    "name": "Airline 1"
                },
                {
                    "id": "2",
                    "name": "Airline 2"
                }
            ]
        },
        {
            "distance": 350.0,
            "transfer_airports": [],
            "airlines": [
                {
                    "id": "1",
                    "name": "Airline 1"
                }
            ]
        }
    ]


def test_prepare_output_data_with_output_ratings() -> None:
    G: nx.DiGraph = nx.DiGraph()
    G.add_nodes_from(["A", "B", "C"])
    G.add_edge("A", "B", weight=100., airline_id="1")
    G.add_edge("B", "C", weight=200., airline_id="2")
    G.add_edge("A", "C", weight=350., airline_id="1")
    shortest_paths: list[list[str]] = [
        ["A", "B", "C"],
        ["A", "C"]
    ]
    airline_id_to_name_map: dict[str, str] = {
        "1": "Airline 1",
        "2": "Airline 2"
    }
    airport_id_to_name_map: dict[str, str] = {
        "A": "Airport A",
        "B": "Airport B",
        "C": "Airport C"
    }
    airline_opinion_data: server.OpinionData = {
        "1": {
            "overall_rating": 1.,
            "seat_comfort": 1.,
            "service_quality": 1.,
            "food_quality": 1.,
            "onboard_entertainment": 1.,
            "quality_price_ratio": 1.
        },
        "2": {
            "overall_rating": 2.,
            "seat_comfort": 2.,
            "service_quality": 2.,
            "food_quality": 2.,
            "onboard_entertainment": 2.,
            "quality_price_ratio": 2.
        }
    }
    airport_opinion_data: server.OpinionData = {
        "A": {
            "overall_rating": 1.,
            "queuing_efficiency": 1.,
            "cleanliness": 1.,
            "shopping_facilities": 1.
        },
        "B": {
            "overall_rating": 2.,
            "queuing_efficiency": 2.,
            "cleanliness": 2.,
            "shopping_facilities": 2.
        },
        "C": {
            "overall_rating": 3.,
            "queuing_efficiency": 3.,
            "cleanliness": 3.,
            "shopping_facilities": 3.
        }
    }

    output_data: server.OutputData = server.prepare_output_data(
        G,
        shortest_paths,
        airline_id_to_name_map,
        airport_id_to_name_map,
        include_ratings_in_output=True,
        airline_opinion_data=airline_opinion_data,
        airport_opinion_data=airport_opinion_data)

    assert output_data == [
        {
            "distance": 300.0,
            "transfer_airports": [
                {
                    "id": "B",
                    "name": "Airport B",
                    "ratings": {
                        "overall_rating": 2.,
                        "queuing_efficiency": 2.,
                        "cleanliness": 2.,
                        "shopping_facilities": 2.
                    }
                }
            ],
            "airlines": [
                {
                    "id": "1",
                    "name": "Airline 1",
                    "ratings": {
                        "overall_rating": 1.,
                        "seat_comfort": 1.,
                        "service_quality": 1.,
                        "food_quality": 1.,
                        "onboard_entertainment": 1.,
                        "quality_price_ratio": 1.
                    }
                },
                {
                    "id": "2",
                    "name": "Airline 2",
                    "ratings": {
                        "overall_rating": 2.,
                        "seat_comfort": 2.,
                        "service_quality": 2.,
                        "food_quality": 2.,
                        "onboard_entertainment": 2.,
                        "quality_price_ratio": 2.
                    }
                }
            ]
        },
        {
            "distance": 350.0,
            "transfer_airports": [],
            "airlines": [
                {
                    "id": "1",
                    "name": "Airline 1",
                    "ratings": {
                        "overall_rating": 1.,
                        "seat_comfort": 1.,
                        "service_quality": 1.,
                        "food_quality": 1.,
                        "onboard_entertainment": 1.,
                        "quality_price_ratio": 1.
                    }
                }
            ]
        }
    ]
