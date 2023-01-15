import * as React from 'react';
import { RatingSlider } from './RatingSlider';
import { Checkbox, Button, Typography, Grid, Paper, Box, Alert, AlertTitle } from '@mui/material';
import Response from './Response';
import buildRequest from './Request';
import Selector from './Selector';
import configData from "./config.json";

export class Browser extends React.Component {
  constructor(props) {
    super(props);
    this.state = initialState()
  };

  renderSearchView() {
    return (
      <Grid container maxWidth={1200} alignItems="center" justify="center">
        {this.state.error !== '' ? <Grid item md={12} sx={{ pb: 5, pt: 5 }}>
          <Alert severity="error">
            <AlertTitle>Error</AlertTitle>
            {this.state.error}
          </Alert>
        </Grid> : <></>}
        <Grid item md={6} sx={{ p: 1 }}>
          <Selector handleSelect={(code) => this.setState({ departure_airport: code })} label="Departure airport" airports={this.state.airports} />
        </Grid>
        <Grid item md={6} sx={{ p: 1 }}>
          <Selector handleSelect={(code) => this.setState({ destination_airport: code })} label="Destination airport" airports={this.state.airports} />
        </Grid>
        <RatingSlider label={'Number of connections'} value={this.state.n_best_connections} onChange={(e) => this.setState({ n_best_connections: e.target.value })} />
        <RatingSlider label={'Distance'} value={this.state.distance} onChange={(e) => this.setState({ distance: e.target.value })} />
        <Grid item xs={6}>
          <Typography gutterBottom sx={{ pr: 3, pl: 3, pt: 1, pb: 1 }}>
            Consider separate components for airline
          </Typography>
        </Grid>
        <Grid item xs={6} >
          <Checkbox color="success" checked={this.state.only_overall_airline} onChange={(e) => this.setState({ only_overall_airline: e.target.checked })} />
        </Grid>
        <Grid item xs={12} ><Paper elevation={5}  >
          {this.renderAirlineRaitings()}
        </Paper></Grid>
        <Grid item xs={6}>
          <Typography gutterBottom sx={{ pr: 3, pl: 3, pt: 1, pb: 1 }}>
            Consider separate components for airport
          </Typography>
        </Grid>
        <Grid item xs={6} >
          <Checkbox color="success" checked={this.state.only_overall_airport} onChange={(e) => this.setState({ only_overall_airport: e.target.checked })} />
        </Grid>
        <Grid item xs={12}>
          <Paper elevation={5} >
            {this.renderAirportRaitings()}
          </Paper>
        </Grid>
        <Grid item xs={12} sx={{ pt: 3 }}>
          <Box textAlign='right'>
            <Button variant="contained" onClick={() => this.getConnections(this.state)} color="success" >Search</Button>
          </Box>
        </Grid>
      </Grid>
    )
  }

  renderAirlineRaitings() {
    if (!this.state.only_overall_airline)
      return <RatingSlider label={"Overall airline rating"} value={this.state.overall_airline} onChange={(e) => this.setState({ overall_airline: e.target.value })} />
    else return (
      <Box>
        <RatingSlider label={"Overall airline rating"} value={this.state.overall_airline} onChange={(e) => this.setState({ overall_airline: e.target.value })} />
        <RatingSlider label={"Seat comfort"} value={this.state.seat_comfort} onChange={(e) => this.setState({ seat_comfort: e.target.value })} />
        <RatingSlider label={"Service quality"} value={this.state.service_quality} onChange={(e) => this.setState({ service_quality: e.target.value })} />
        <RatingSlider label={"Food quality"} value={this.state.food_quality} onChange={(e) => this.setState({ food_quality: e.target.value })} />
        <RatingSlider label={"Onboard Entertainment"} value={this.state.onboard_entertainment} onChange={(e) => this.setState({ onboard_entertainment: e.target.value })} />
        <RatingSlider label={"Quality Price Ratio"} value={this.state.quality_price_ratio} onChange={(e) => this.setState({ quality_price_ratio: e.target.value })} />
      </Box>
    )
  }

  renderAirportRaitings() {
    if (!this.state.only_overall_airport)
      return <RatingSlider label={"Overall airport rating"} value={this.state.overall_airport} onChange={(e) => this.setState({ overall_airport: e.target.value })} />
    else return (
      <Box>
        <RatingSlider label={"Overall airport rating"} value={this.state.overall_airport} onChange={(e) => this.setState({ overall_airport: e.target.value })} />
        <RatingSlider label={"Queuing Efficiency"} value={this.state.queuing_efficiency} onChange={(e) => this.setState({ queuing_efficiency: e.target.value })} />
        <RatingSlider label={"Cleanliness"} value={this.state.cleanliness} onChange={(e) => this.setState({ cleanliness: e.target.value })} />
        <RatingSlider label={"Shopping Facilities"} value={this.state.shopping_facilities} onChange={(e) => this.setState({ shopping_facilities: e.target.value })} />
      </Box>
    )
  }

  renderResponseView() {
    return (
      <Response
        returnFun={(e) => this.setState(initialState(this.state.airports))}
        connections={this.state.response}
        departure_airport={this.state.departure_airport}
        destination_airport={this.state.destination_airport}
        airports={this.state.airports}
      />
    )
  }

  render() {
    if (this.state.airports.length !== 0)
      if (this.state.searchMode)
        return this.renderSearchView()
      else
        return this.renderResponseView()
    else return (<></>)
  }

  getConnections(state) {
    if (state.destination_airport != null && state.departure_airport != null && state.destination_airport !== state.departure_airport) {
      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(buildRequest(state))
      };

      fetch(configData.connectionsEndpoint, requestOptions)
        .then(response => response.json())
        .then(data => {
          if (data.length !== 0)
            this.setState({ response: data, searchMode: false })
          else
            this.setState({ error: 'No connections were found.' })
        });
    } else {
      this.setState({ error: 'You must provide both departure and destination airports.' })
    }
  }

  componentDidMount() {
    const requestOptions = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    };
    fetch(configData.airportsEndpoint, requestOptions)
      .then(response => response.json())
      .then(airports =>
        this.setState({ airports: airports.map(a => ({ key: a.id, label: a.name })) }))

  }
}

function initialState(airports = []) {
  return {
    departure_airport: null,
    destination_airport: null,
    n_best_connections: 5,
    distance: 5,
    seat_comfort: 5,
    service_quality: 5,
    food_quality: 5,
    onboard_entertainment: 5,
    quality_price_ratio: 5,
    queuing_efficiency: 5,
    cleanliness: 5,
    shopping_facilities: 5,
    overall_airline: 5,
    overall_airport: 5,
    only_overall_airport: false,
    only_overall_airline: false,
    response: null,
    searchMode: true,
    error: '',
    include_ratings_in_output: true,
    airports: airports
  }
}
