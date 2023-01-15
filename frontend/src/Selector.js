import React, { useState, useMemo } from "react";
import {
  Box,
  FormControl,
  Select,
  MenuItem,
  InputLabel,
  ListSubheader,
  TextField,
  InputAdornment
} from "@mui/material";
import SearchIcon from '@mui/icons-material/Search';
import DataUtils from './DataUtils';


const containsText = (text, searchText) =>
  text.toLowerCase().indexOf(searchText.toLowerCase()) > -1;

const airports = DataUtils.allAirports();

export default function Selector(props) {
  const [airport, setAirport] = useState(airports[0]);

  const [filter, setFilter] = useState("");

  const filteredAirports = useMemo(
    () => airports.filter((airport) => containsText(airport.key, filter) || containsText(airport.label, filter)),
    [filter]
  );

  return (
    <Box>
      <FormControl fullWidth>
        <InputLabel id="search-select-label">Airport</InputLabel>
        <Select
          MenuProps={{ autoFocus: false }}
          labelId="search-select-label"
          id="search-select"
          value={airport.label}
          label="Options"
          onChange={(e) => {
            let airport = filteredAirports.find( a => a.label === e.target.value )
            setAirport(airport)
            props.handleSelect(airport.key)
          }}
          onClose={() => setFilter("")}
          renderValue={() => airport.label}
        >
          <ListSubheader>
            <TextField
              size="small"
              autoFocus
              placeholder="Type to search..."
              fullWidth
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <SearchIcon />
                  </InputAdornment>
                )
              }}
              onChange={(e) => setFilter(e.target.value)}
              onKeyDown={(e) => {
                if (e.key !== "Escape") {
                  e.stopPropagation();
                }
              }}
            />
          </ListSubheader>
          {filteredAirports.map((airport, i) => (
            <MenuItem key={airport.key} value={airport.label}>
              {airport.label}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
  );
}
