from pathlib import Path

import pandas as pd
from fastapi import FastAPI, Response, Depends
import uvicorn

from .input_schema import BestPathsInputData
from .read_data import read_opinion_data, OpinionData

app = FastAPI()

def read_data_on_startup(data_path: Path) -> tuple[OpinionData, OpinionData, pd.DataFrame]:
    airline_opinion_data: OpinionData = read_opinion_data(data_path / "airlines.csv")
    airport_opinion_data: OpinionData = read_opinion_data(data_path / "airlines.csv")
    flights: pd.DataFrame = pd.read_csv(data_path / "airlines.csv")
    return airline_opinion_data, airport_opinion_data, flights

@app.post("/")
async def get_best_paths(
        best_paths_input_data: BestPathsInputData,
        static_data: tuple[OpinionData, OpinionData, pd.DataFrame] = Depends(read_data_on_startup(Path("mock_data")))) -> Response:
    return best_paths_input_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)