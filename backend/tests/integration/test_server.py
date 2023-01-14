from pathlib import Path
import json

from fastapi.testclient import TestClient
from httpx import Response

import server

client = TestClient(server.app)


def test_get_best_paths_happy_path() -> None:
    server.data_reader.set_data_path(Path("mock_data"))
    with open("sample_request.json", "r") as input_json_file:
        input_data: dict = json.load(input_json_file)
    with open("sample_response.json", "r") as output_json_file:
        expected_output_data: dict = json.load(output_json_file)

    response: Response = client.post("/", json=input_data)

    assert response.status_code == 200
    assert response.json() == expected_output_data


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
