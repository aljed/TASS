import * as React from 'react';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

export default function Flight(flightData) {

  const distance = flightData.distance
  const destinationAirports = flightData.destinationAirports

  return (
    <Accordion>
      <AccordionSummary
        expandIcon={<ExpandMoreIcon />}
        aria-controls="panel1a-content"
        id="panel1a-header"
      >
        <Typography>distance</Typography>
      </AccordionSummary>
      <AccordionDetails>
        <Typography>
          aaa
        </Typography>
      </AccordionDetails>
    </Accordion>
  );
}
