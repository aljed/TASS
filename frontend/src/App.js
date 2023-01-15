import * as React from 'react';
import { Browser } from './Browser';
import { Box, Grid, Typography } from '@mui/material';
import AirplanemodeActive from '@mui/icons-material/AirplanemodeActive';


export default class App extends React.Component {
  render() {
    return (
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        minHeight="100vh"
      >
        <Grid container maxWidth={1200}>
          <Grid item md={1}>
            <AirplanemodeActive color="success" sx={{ fontSize: 70 }} />
          </Grid>
          <Grid item md={11}>
            <Typography variant="h2" gutterBottom>
              Flight Browser
            </Typography>
          </Grid>
          <Grid item md={12}>
            <Browser />
          </Grid>
        </Grid>
      </Box>
    )
  }
}
