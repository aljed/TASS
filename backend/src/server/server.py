import argparse
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, Response, Depends
import uvicorn
import networkx as nx

from .input_schema import BestPathsInputData
from .read_data import OpinionData, StaticData, DataReader
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
    airport_opinion_data: OpinionData
    flights: pd.DataFrame
    airline_opinion_data, airport_opinion_data, flights = static_data

    G: nx.DiGraph = construct_graph(
        flights, airline_opinion_data, airport_opinion_data, best_paths_input_data.rating_weights)
    
    shortest_paths: list[list[str]] = get_shortest_paths(
        G,
        best_paths_input_data.departure_airport_id,
        best_paths_input_data.destination_airport_id,
        best_paths_input_data.n_best_connections)
    return prepare_output_data(G, shortest_paths)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, default="mock_data", help="Path to directory with data files")
    parser.add_argument("--port", type=int, default=3000, help="Port the server should listen on")
    args = parser.parse_args()
    data_reader.set_data_path(Path(args.data_path))
    uvicorn.run(app, port=args.port)
