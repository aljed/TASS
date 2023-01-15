from pathlib import Path
import json

from fastapi.testclient import TestClient
from httpx import Response

import server

client = TestClient(server.app)


def test_get_all_airports_happy_path() -> None:
    server.data_reader.set_data_path(Path("mock_data"))
    with open("sample_requests_and_responses/get_all_airports/response.json", "r") as output_json_file:
        expected_output_data: dict = json.load(output_json_file)

    response: Response = client.get("/airports")

    assert response.status_code == 200
    assert response.json() == expected_output_data
