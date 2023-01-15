import argparse
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, Response, Depends, HTTPException
import uvicorn
import networkx as nx

from .input_schema import BestPathsInputData
from .data_reader import OpinionData, StaticData, DataReader
from .construct_graph import construct_graph
from .get_shortest_paths import get_shortest_paths
from .prepare_output_data import prepare_output_data

app = FastAPI()
data_reader = DataReader()


@app.post("/")
async def get_best_paths(
        best_paths_input_data: BestPathsInputData,
        static_data: StaticData = Depends(data_reader)) -> Response:
    airline_opinion_data: OpinionData
    airline_id_to_name_map: dict[str, str]
    airport_opinion_data: OpinionData
    airport_id_to_name_map: dict[str, str]
    flights: pd.DataFrame
    (
        airline_opinion_data,
        airline_id_to_name_map,
        airport_opinion_data,
        airport_id_to_name_map,
        flights
    ) = static_data

    departure_airport_id: str = best_paths_input_data.departure_airport_id
    destination_airport_id: str = best_paths_input_data.destination_airport_id
    
    if departure_airport_id not in airport_id_to_name_map:
        raise HTTPException(
            status_code=404,
            detail=f"Departure airport id {departure_airport_id} not found in list of airports")
    if destination_airport_id not in airport_id_to_name_map:
        raise HTTPException(
            status_code=404,
            detail=f"Destination airport id {destination_airport_id} not found in list of airports")

    G: nx.DiGraph = construct_graph(
        flights, airline_opinion_data, airport_opinion_data, best_paths_input_data.rating_weights)

    shortest_paths: list[list[str]] = get_shortest_paths(
        G,
        departure_airport_id,
        destination_airport_id,
        best_paths_input_data.n_best_connections)
        
    return prepare_output_data(
        G,
        shortest_paths,
        airline_id_to_name_map,
        airport_id_to_name_map,
        best_paths_input_data.include_ratings_in_output,
        airline_opinion_data,
        airport_opinion_data)


@app.get("/airports")
async def get_all_airports(static_data: StaticData = Depends(data_reader)) -> Response:
    airport_id_to_name_map: dict[str, str]
    _, _, _, airport_id_to_name_map, _ = static_data

    airport_ids: list[str] = list(airport_id_to_name_map)
    return [{
            "id": airport_id,
            "name": airport_id_to_name_map[airport_id]
            } for airport_id in airport_ids]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, default="mock_data", help="Path to directory with data files")
    parser.add_argument("--port", type=int, default=3000, help="Port the server should listen on")
    args = parser.parse_args()
    data_reader.set_data_path(Path(args.data_path))
    uvicorn.run(app, port=args.port)
