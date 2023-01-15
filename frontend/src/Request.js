export default function buildRequest(state) {

    var request = {
        departure_airport_id: state.departure_airport,
        destination_airport_id: state.destination_airport,
        n_best_connections: state.n_best_connections,
        rating_weights: {
            distance: state.distance / 10,
            overall_airport: state.overall_airport / 10,
            overall_airline: state.overall_airline / 10
        },
        include_ratings_in_output: true
    }

    if (state.only_overall_airport) {
        request['rating_weights']['airport_components'] = {
            queuing_efficiency: state.queuing_efficiency / 10,
            cleanliness: state.cleanliness / 10,
            shopping_facilities: state.shopping_facilities / 10,
        }
    }

    if (state.only_overall_airline) {
        request['rating_weights']['airline_components'] = {
            seat_comfort: state.seat_comfort / 10,
            service_quality: state.service_quality / 10,
            food_quality: state.food_quality / 10,
            onboard_entertainment: state.overall_airport / 10,
            quality_price_ratio: state.quality_price_ratio / 10
        }
    }

    return request
}
