import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import DoubleArrowIcon from '@mui/icons-material/DoubleArrow';
import Grid from '@mui/material/Grid';
import { Button, Box } from '@mui/material';
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';
import MyPopover from './MyPopover';

export default function Response(props) {

  function getLabelByKey(key) {
    return props.airports.find(airport => airport.key === key).label
  }

  function airportsHeader(airports, dep, dest) {
    var copied = []
    if (airports !== undefined)
      copied = airports.slice()
    copied.unshift(dep)
    copied.push(dest)
    return copied.map((airport) => {
      if (airport !== copied.at(-1))
        return (<><Grid item>{getLabelByKey(airport)}</Grid><Grid item><KeyboardArrowRightIcon color="success" /> </Grid></>)
      else
        return <Grid>{getLabelByKey(airport)}</Grid>
    })
  }

  function showConnections() {
    return props.connections.map(connection => {
      return (<Accordion>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Grid container md={12} >
            <Grid container md={10}>
              {airportsHeader(connection.transfer_airports.map(a => a.id), props.departure_airport, props.destination_airport)}
            </Grid>
            <Grid item md={2}>
              <Box textAlign='right'>
                <Typography sx={{ pr: 3 }}>{connection.distance.toFixed(1)} km</Typography>
              </Box>
            </Grid>
          </Grid>
        </AccordionSummary>
        <AccordionDetails>
          {airportsList(connection.transfer_airports, props.departure_airport, props.destination_airport, connection.airlines)}
        </AccordionDetails>
      </Accordion>
      )
    })
  }

  function airportsList(airports, dep, dest, airlines) {
    var copied = []
    if (airports !== undefined)
      copied = airports.slice()
    copied.unshift(dep)
    copied.push(dest)
    return copied.map((airport, i) => {
      if (airport !== copied.at(-1))
        return (
          <Grid container md={12}>
            <Grid item md={3}>
              {airport === dep ? <Typography>{getLabelByKey(dep)}</Typography> : <MyPopover entity={airport} isAirport={true} />}
            </Grid>
            <Grid item md={1}>
              <DoubleArrowIcon color="success" />
            </Grid>
            <Grid item md={3}>
              {copied.at(i + 1) === dest ? <Typography>{getLabelByKey(dest)}</Typography> : <MyPopover entity={copied.at(i + 1)} isAirport={true} />}
            </Grid>
            <Grid item md={3}></Grid>
            <Grid item md={2}>
              <MyPopover entity={airlines.at(i)} isAirport={false} />
            </Grid>
          </Grid>)
      else return <span />
    })
  }

  return (
    <Box>
      <Grid container maxWidth={1200} sx={{ p: 2 }} alignItems="center" justify="center" >
        <Grid item >
          <Typography variant="h4"  >
            {getLabelByKey(props.departure_airport)}
          </Typography>
        </Grid>
        <Grid item sx={{ pr: 3, pl: 3 }}>
          <DoubleArrowIcon color="success" />
        </Grid>
        <Grid item >
          <Typography variant="h4" >
            {getLabelByKey(props.destination_airport)}
          </Typography>
        </Grid>
      </Grid>
      {showConnections()}
      <Grid item md={12} sx={{ pt: 3 }}>
        <Box textAlign='right'>
          <Button variant="contained" onClick={props.returnFun} color="success">Return to browser</Button>
        </Box>
      </Grid>
    </Box>
  );
}
