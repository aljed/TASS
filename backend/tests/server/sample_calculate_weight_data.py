from typing import Any

import server

def get_airline_opinion_data(airline_id: str) -> server.OpinionData:
    return {
        airline_id: {
            "overall_rating": 5.,
            "seat_comfort": 5.,
            "service_quality": 5.,
            "food_quality": 5.,
            "onboard_entertainment": 5.,
            "quality_price_ratio": 5.
        }
    }

def get_airport_opinion_data(airport_id: str) -> server.OpinionData:
    return {
        airport_id: {
            "overall_rating": 5.,
            "queuing_efficiency": 5.,
            "cleanliness": 5.,
            "shopping_facilities": 5.
        }
    }

def get_rating_weights_without_components() -> dict[str, Any]:
    return {
        "distance": 1.,
        "overall_airline": 1.,
        "overall_airport": 1.
    }

def get_rating_weights_with_airline_component() -> dict[str, Any]:
    return {
        "distance": 1.,
        "overall_airline": 1.,
        "airline_components": {
            "seat_comfort": 1.,
            "service_quality": 1.,
            "food_quality": 1.,
            "onboard_entertainment": 1.,
            "quality_price_ratio": 1.
        },
        "overall_airport": 1.
    }

def get_rating_weights_with_airport_component() -> dict[str, Any]:
    return {
        "distance": 1.,
        "overall_airline": 1.,
        "overall_airport": 1.,
        "airport_components": {
            "queuing_efficiency": 1.,
            "cleanliness": 1.,
            "shopping_facilities": 1.
        }
    }

def get_rating_weights_with_all_components() -> dict[str, Any]:
    return {
        "distance": 1.,
        "overall_airline": 1.,
        "airline_components": {
            "seat_comfort": 1.,
            "service_quality": 1.,
            "food_quality": 1.,
            "onboard_entertainment": 1.,
            "quality_price_ratio": 1.
        },
        "overall_airport": 1.,
        "airport_components": {
            "queuing_efficiency": 1.,
            "cleanliness": 1.,
            "shopping_facilities": 1.
        }
    }