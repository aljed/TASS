from pathlib import Path
import json

from fastapi.testclient import TestClient
from httpx import Response

import server

client = TestClient(server.app)


def test_get_best_paths_happy_path() -> None:
    server.data_reader.set_data_path(Path("mock_data"))
    with open("sample_requests_and_responses/get_best_paths/request.json", "r") as input_json_file:
        input_data: dict = json.load(input_json_file)
    with open("sample_requests_and_responses/get_best_paths/response.json", "r") as output_json_file:
        expected_output_data: dict = json.load(output_json_file)

    response: Response = client.post("/", json=input_data)

    assert response.status_code == 200
    assert response.json() == expected_output_data


def test_get_best_paths_happy_path_no_ratings_in_output() -> None:
    server.data_reader.set_data_path(Path("mock_data"))
    input_data: dict = {
        "departure_airport_id": "WAW",
        "destination_airport_id": "MUC",
        "n_best_connections": 2,
        "rating_weights": {
            "distance": 1.0,
            "overall_airline": 1.0,
            "airline_components": {
                "seat_comfort": 0.0,
                "service_quality": 0.0,
                "food_quality": 0.0,
                "onboard_entertainment": 0.0,
                "quality_price_ratio": 1.0
            },
            "overall_airport": 1.0,
            "airport_components": {
                "queuing_efficiency": 0.0,
                "cleanliness": 1.0,
                "shopping_facilities": 0.0
            }
        }
    }

    response: Response = client.post("/", json=input_data)

    assert response.status_code == 200
    assert response.json() == [
        {
            "distance": 2760.0,
            "transfer_airports": [],
            "airlines": [
                {
                    "id": "RYANAIR",
                    "name": "Ryanair"
                }
            ]
        },
        {
            "distance": 3550.0,
            "transfer_airports": [
                {
                    "id": "KRK",
                    "name": "Cracow"
                }
            ],
            "airlines": [
                {
                    "id": "RYANAIR",
                    "name": "Ryanair"
                },
                {
                    "id": "LOT",
                    "name": "Lot"
                }
            ]
        }
    ]


def test_get_best_paths_invalid_schema_fail() -> None:
    server.data_reader.set_data_path(Path("mock_data"))
    invalid_input_data: dict = {
        "illegal_field": "hello",
        "departure_airport_id": "WAW",
        "destination_airport_id": "MUC",
        "n_best_connections": 2,
        "rating_weights": {
            "distance": 1.0,
            "overall_airline": 1.0,
            "overall_airport": 1.0
        }
    }

    response: Response = client.post("/", json=invalid_input_data)

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "illegal_field"
                ],
                "msg": "extra fields not permitted",
                "type": "value_error.extra"
            }
        ]
    }


def test_get_best_paths_departure_airport_id_not_found_fail() -> None:
    server.data_reader.set_data_path(Path("mock_data"))
    invalid_input_data: dict = {
        "departure_airport_id": "UNKNOWN",
        "destination_airport_id": "MUC",
        "n_best_connections": 2,
        "rating_weights": {
            "distance": 1.0,
            "overall_airline": 1.0,
            "overall_airport": 1.0
        }
    }

    response: Response = client.post("/", json=invalid_input_data)

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Departure airport id UNKNOWN not found in list of airports"
    }


def test_get_best_paths_destination_airport_id_not_found_fail() -> None:
    server.data_reader.set_data_path(Path("mock_data"))
    invalid_input_data: dict = {
        "departure_airport_id": "WAW",
        "destination_airport_id": "UNKNOWN",
        "n_best_connections": 2,
        "rating_weights": {
            "distance": 1.0,
            "overall_airline": 1.0,
            "overall_airport": 1.0
        }
    }

    response: Response = client.post("/", json=invalid_input_data)

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Destination airport id UNKNOWN not found in list of airports"
    }
