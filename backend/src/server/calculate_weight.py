from typing import Any

from .read_data import OpinionData


def calculate_weight(
        airline_id: str,
        airport_id: str,
        distance: float,
        airline_opinion_data: OpinionData,
        airport_opinion_data: OpinionData,
        rating_weights: dict[str, Any]) -> float:

    airline_weight: float = __calculate_airline_weight(airline_id, airline_opinion_data, rating_weights)
    airport_weight: float = __calculate_airport_weight(airport_id, airport_opinion_data, rating_weights)
    total_weight: float = distance * (rating_weights["distance"] + airline_weight + airport_weight)
    return total_weight


def __calculate_airline_weight(
        airline_id: str,
        airline_opinion_data: OpinionData,
        rating_weights: dict[str, Any]) -> float:

    airline_specific_opinion_data: dict[str, float] = airline_opinion_data[airline_id]
    overall_rating: float = airline_specific_opinion_data["overall_rating"]
    overall_airline_weight = rating_weights["overall_airline"]
    airline_weight: float = (1 - overall_rating / 10) * overall_airline_weight
    if "airline_components" in rating_weights:
        for component_name in __get_all_rating_components(airline_specific_opinion_data):
            component_rating = airline_specific_opinion_data[component_name]
            component_weight = rating_weights["airline_components"][component_name]
            airline_weight += (1 - component_rating / 10) * component_weight
    return airline_weight


def __calculate_airport_weight(
        airport_id: str,
        airport_opinion_data: OpinionData,
        rating_weights: dict[str, Any]) -> float:

    airport_specific_opinion_data: dict[str, float] = airport_opinion_data[airport_id]
    overall_rating: float = airport_specific_opinion_data["overall_rating"]
    overall_airport_weight = rating_weights["overall_airport"]
    airport_weight: float = (1 - overall_rating / 10) * overall_airport_weight
    if "airport_components" in rating_weights:
        for component_name in __get_all_rating_components(airport_specific_opinion_data):
            component_rating = airport_specific_opinion_data[component_name]
            component_weight = rating_weights["airport_components"][component_name]
            airport_weight += (1 - component_rating / 10) * component_weight
    return airport_weight


def __get_all_rating_components(item_specific_opinion_data: dict[str, float]) -> list[str]:
    all_rating_components: list[str] = list(item_specific_opinion_data)
    all_rating_components.remove("overall_rating")
    return all_rating_components
