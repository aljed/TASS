import * as React from 'react';
import { Browser } from './Browser';
import { Box} from '@mui/material';


export default function SelectAirport() {
  return (
    <Box
      display="flex"
      justifyContent="center"
      alignItems="center"
      minHeight="100vh"
    >
      <Browser />
    </Box>
  );
}
