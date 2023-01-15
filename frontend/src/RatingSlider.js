import * as React from 'react';
import Slider from '@mui/material/Slider';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';


const marks = [
  {
    value: 0,
    label: '0',
  },
  {
    value: 10,
    label: '10',
  },
];

export class RatingSlider extends React.Component {
  render() {
    return (
      <Grid container alignItems="center" justify="center">
        <Grid item xs={6} sx={{ pr: 3, pl: 3, pt: 1, pb: 1 }}>
          <Typography id="input-slider" gutterBottom>
            {this.props.label}
          </Typography>
        </Grid>
        <Grid item xs={6} sx={{ pr: 3, pl: 3, pt: 1, pb: 1 }}>
          <Slider
            color="success"
            value={this.props.value}
            aria-labelledby="input-slider"
            step={1}
            min={0}
            max={10}
            aria-label="Restricted values"
            onChange={this.props.onChange}
            marks={marks}
            key={this.props.label}
          />
        </Grid>
      </Grid>
    )
  }
}