import server
from sample_calculate_weight_data import *


def test_calculate_weight_without_components() -> None:
    airline_id: str = "airline1"
    airport_id: str = "airport1"
    distance: int = 100
    airline_opinion_data: server.OpinionData = get_airline_opinion_data(airline_id)
    airport_opinion_data: server.OpinionData = get_airport_opinion_data(airport_id)
    rating_weights = get_rating_weights_without_components()
    
    weight: float = server.calculate_weight(
        airline_id, airport_id, distance, airline_opinion_data, airport_opinion_data, rating_weights)
    
    assert weight == 200.

def test_calculate_weight_with_airline_component() -> None:
    airline_id: str = "airline1"
    airport_id: str = "airport1"
    distance: int = 100
    airline_opinion_data: server.OpinionData = get_airline_opinion_data(airline_id)
    airport_opinion_data: server.OpinionData = get_airport_opinion_data(airport_id)
    rating_weights = get_rating_weights_with_airline_component()
    
    weight: float = server.calculate_weight(
        airline_id, airport_id, distance, airline_opinion_data, airport_opinion_data, rating_weights)
    
    assert weight == 450.

def test_calculate_weight_with_airport_component() -> None:
    airline_id: str = "airline1"
    airport_id: str = "airport1"
    distance: int = 100
    airline_opinion_data: server.OpinionData = get_airline_opinion_data(airline_id)
    airport_opinion_data: server.OpinionData = get_airport_opinion_data(airport_id)
    rating_weights = get_rating_weights_with_airport_component()
    
    weight: float = server.calculate_weight(
        airline_id, airport_id, distance, airline_opinion_data, airport_opinion_data, rating_weights)
    
    assert weight == 350.

def test_calculate_weight_with_all_components() -> None:
    airline_id: str = "airline1"
    airport_id: str = "airport1"
    distance: int = 100
    airline_opinion_data: server.OpinionData = get_airline_opinion_data(airline_id)
    airport_opinion_data: server.OpinionData = get_airport_opinion_data(airport_id)
    rating_weights = get_rating_weights_with_all_components()
    
    weight: float = server.calculate_weight(
        airline_id, airport_id, distance, airline_opinion_data, airport_opinion_data, rating_weights)
    
    assert weight == 600.