import * as React from 'react';
import { RatingSlider } from './RatingSlider';
import { Checkbox, Button, Typography, Grid, Paper } from '@mui/material';
import Response from './Response';
import buildRequest from './Request';
import Selector from './Selector';

export class Browser extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
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
      searchMode: true
    }
  };

  renderSearchView() {
    return (
      <Grid container width={500} >
        <Grid xs={6}>
          <Selector handleSelect={(code) => this.setState({ departure_airport: code })} />
        </Grid>
        <Grid xs={6}>
          <Selector handleSelect={(code) => this.setState({ destination_airport: code })} />
        </Grid>
        <Grid container >
          <RatingSlider label={'Number of connections'} value={this.state.n_best_connections} onChange={(e) => this.setState({ n_best_connections: e.target.value })} />
          <RatingSlider label={'Distance'} value={this.state.distance} onChange={(e) => this.setState({ distance: e.target.value })} />
          <Grid xs={8}>
            <Typography gutterBottom>
              Consider separate components for airline
            </Typography>
          </Grid>
          <Grid xs={4}>
            <Checkbox checked={this.state.only_overall_airline} onChange={(e) => this.setState({ only_overall_airline: e.target.checked })} />
          </Grid>
          <Paper elevation={1} >
            {this.renderAirlineRaitings()}
          </Paper>
          <Grid xs={8}>
            <Typography gutterBottom>
              Consider separate components for airport
            </Typography>
          </Grid>
          <Grid xs={4}>
            <Checkbox checked={this.state.only_overall_airport} onChange={(e) => this.setState({ only_overall_airport: e.target.checked })} />
          </Grid>
          <Paper elevation={1} >
            {this.renderAirportRaitings()}
          </Paper>
          <Button variant="contained" onClick={() => this.getConnections(this.state)}>Search</Button>
        </Grid>
      </Grid>
    )
  }

  renderAirlineRaitings() {
    if (!this.state.only_overall_airline)
      return <RatingSlider label={"Overall airline rating"} value={this.state.overall_airline} onChange={(e) => this.setState({ overall_airline: e.target.value })} />
    else return (
      <div>
        <RatingSlider label={"Seat comfort"} value={this.state.seat_comfort} onChange={(e) => this.setState({ seat_comfort: e.target.value })} />
        <RatingSlider label={"Service quality"} value={this.state.service_quality} onChange={(e) => this.setState({ service_quality: e.target.value })} />
        <RatingSlider label={"Food quality"} value={this.state.food_quality} onChange={(e) => this.setState({ food_quality: e.target.value })} />
        <RatingSlider label={"Onboard Entertainment"} value={this.state.onboard_entertainment} onChange={(e) => this.setState({ onboard_entertainment: e.target.value })} />
        <RatingSlider label={"Quality Price Ratio"} value={this.state.quality_price_ratio} onChange={(e) => this.setState({ quality_price_ratio: e.target.value })} />
      </div>
    )
  }

  renderAirportRaitings() {
    if (!this.state.only_overall_airport)
      return <RatingSlider label={"Overall airport rating"} value={this.state.overall_airport} onChange={(e) => this.setState({ overall_airport: e.target.value })} />
    else return (
      <div>
        <RatingSlider label={"Queuing Efficiency"} value={this.state.queuing_efficiency} onChange={(e) => this.setState({ queuing_efficiency: e.target.value })} />
        <RatingSlider label={"Cleanliness"} value={this.state.cleanliness} onChange={(e) => this.setState({ cleanliness: e.target.value })} />
        <RatingSlider label={"Shopping Facilities"} value={this.state.shopping_facilities} onChange={(e) => this.setState({ shopping_facilities: e.target.value })} />
      </div>
    )
  }

  renderResponseView() {
    return (
      <Response 
        returnFun={(e) => this.setState({ searchMode: true })} 
        connections={this.state.response} 
        departure_airport={this.state.departure_airport}
        destination_airport={this.state.destination_airport}
      />
    )
  }

  render() {
    if (this.state.searchMode)
      return this.renderSearchView()
    else
      return this.renderResponseView()
  }

  getConnections(state) {
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(buildRequest(state))
    };

    fetch('http://localhost:3001/search', requestOptions)
      .then(response => response.json())
      .then(data => this.setState({ response: data, searchMode: false }));
  }
}