from pydantic import BaseModel

class AirlineRatingWeightsComponents(BaseModel):
    seat_comfort: float
    service_quality: float
    food_quality: float
    onboard_entertainment: float
    quality_price_ratio: float

class AirportRatingWeightsComponents(BaseModel):
    queuing_efficiency: float
    cleanliness: float
    shopping_facilities: float

class RatingWeights(BaseModel):
    distance: float
    overall_airline: float
    airline_components: AirlineRatingWeightsComponents = None
    overall_airport: float
    airport_components: AirportRatingWeightsComponents = None

class BestPathsInputData(BaseModel):
    departure_airport_id: str
    destination_airport_id: str
    n_best_connections: int
    include_ratings_in_output: bool = False
    rating_weights: RatingWeights
    class Config:
        extra = "forbid"