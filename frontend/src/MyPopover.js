import * as React from 'react';
import Popover from '@mui/material/Popover';
import Typography from '@mui/material/Typography';
import { Grid, Box } from '@mui/material';

export default function MyPopover(props) {
  const [anchorEl, setAnchorEl] = React.useState(null);

  const handlePopoverOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handlePopoverClose = () => {
    setAnchorEl(null);
  };

  const open = Boolean(anchorEl);

  function renderAirlineParameters() {
    return (
      <Grid container md={12} sx={{ p: 1 }}>
        <Grid item xs={11}>Overall airline rating</Grid><Grid item xs={1}>{props.entity.ratings.overall_rating}</Grid>
        <Grid item xs={11}>Seat comfort</Grid><Grid item xs={1}>{props.entity.ratings.seat_comfort}</Grid>
        <Grid item xs={11}>Service quality</Grid><Grid item xs={1}>{props.entity.ratings.service_quality}</Grid>
        <Grid item xs={11}>Food quality</Grid><Grid item xs={1}>{props.entity.ratings.food_quality}</Grid>
        <Grid item xs={11}>Onboard Entertainment</Grid><Grid item xs={1}>{props.entity.ratings.onboard_entertainment}</Grid>
        <Grid item xs={11}>Quality Price Ratio</Grid><Grid item xs={1}>{props.entity.ratings.quality_price_ratio}</Grid>
      </Grid>
    )
  }

  function renderAirportParameters() {
    return (
      <Grid container md={12} sx={{ p: 1 }}>
        <Grid item xs={11}>Overall airport rating</Grid><Grid item xs={1}>{props.entity.ratings.overall_rating}</Grid>
        <Grid item xs={11}>Queuing Efficiency</Grid><Grid item xs={1}>{props.entity.ratings.queuing_efficiency}</Grid>
        <Grid item xs={11}>Cleanliness</Grid><Grid item xs={1}>{props.entity.ratings.cleanliness}</Grid>
        <Grid item xs={11}>Shopping Facilities</Grid><Grid item xs={1}>{props.entity.ratings.shopping_facilities}</Grid>
      </Grid>
    )
  }

  function renderParameters() {
    if (props.isAirport)
      return renderAirportParameters()
    else
      return renderAirlineParameters()
  }

  return (
    <Box>
      <Typography
        aria-owns={open ? 'mouse-over-popover' : undefined}
        aria-haspopup="true"
        onMouseEnter={handlePopoverOpen}
        onMouseLeave={handlePopoverClose}
      >
        {props.entity.name}
      </Typography>
      <Popover
        id="mouse-over-popover"
        sx={{
          pointerEvents: 'none',
        }}
        open={open}
        anchorEl={anchorEl}
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'left',
        }}
        transformOrigin={{
          vertical: 'top',
          horizontal: 'left',
        }}
        onClose={handlePopoverClose}
        disableRestoreFocus
      >
        <Box maxWidth={250}>
          {renderParameters()}
        </Box>
      </Popover>
    </Box>
  );
}
