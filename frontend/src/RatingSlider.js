import * as React from 'react';
import Slider from '@mui/material/Slider';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';


export class RatingSlider extends React.Component {
  render() {
    return (
        <Box sx={{ width: 500 }}>
          <Grid container >
            <Grid xs={6}>
              <Typography id="input-slider" gutterBottom>
                {this.props.label}
              </Typography>
            </Grid>
            <Grid xs={6}>
              <Slider
                defaultValue={this.props.value}
                // onChange={handleSliderChange}
                aria-labelledby="input-slider"
                step={1}
                min={0}
                max={10}
                aria-label="Restricted values"
                onChange={this.props.onChange}
              />
            </Grid>
          </Grid>
        </Box>
      )
  }
}