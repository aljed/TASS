import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import DoubleArrowIcon from '@mui/icons-material/DoubleArrow';
import Grid from '@mui/material/Grid';
import { Button } from '@mui/material';


export default function Response(props) {

  function airportsHeader(airports, dep, dest) {
    var copied = []
    if (airports !== undefined)
      copied = airports.slice()
    copied.unshift(dep)
    copied.push(dest)
    return copied.map( (airport) => {
      if (airport !== copied.at(-1))
        return <span>{airport} <DoubleArrowIcon color="blue" /></span>
      else 
        return <span>{airport}</span>
    })
  }

  function airportsList(airports, dep, dest, airline_ids) {
    console.log(airline_ids)
    var copied = []
    if (airports !== undefined)
      copied = airports.slice()
    copied.unshift(dep)
    copied.push(dest)
    return copied.map( (airport, i) => {
      if (airport !== copied.at(-1))
        return <p>{airport} <DoubleArrowIcon color="blue" /> {copied.at(i+1)} {airline_ids.at(i)}</p>
      else return <span />
    })
  }
  
  function showConnections() {
    return props.connections.map( connection => {
      return (<Accordion>
        <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography>{airportsHeader(connection.transfer_airport_ids, props.departure_airport, props.destination_airport)}</Typography>
        </AccordionSummary>
        <AccordionDetails>
          <Typography>{airportsList(connection.transfer_airport_ids, props.departure_airport, props.destination_airport, connection.airline_ids)}</Typography>
        </AccordionDetails>
      </Accordion>
      )
    })
  }

  return (
    <div>
      <Grid container spacing={0}>
        <Grid xs={5}>
          <Typography variant="h4" gutterBottom>
            {props.departure_airport}
          </Typography>
        </Grid>
        <Grid xs={2}>
          <DoubleArrowIcon color="blue" />
        </Grid>
        <Grid xs={5}>
          <Typography variant="h4" gutterBottom>
            {props.destination_airport}
          </Typography>
        </Grid>
      </Grid>
      {showConnections()}
      <Button variant="contained" onClick={props.returnFun}>Return to browser</Button>
    </div>
  );
}
