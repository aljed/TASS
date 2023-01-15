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


const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      autoFocus: false
    },
  },
};

const containsText = (text, searchText) =>
  text.toLowerCase().indexOf(searchText.toLowerCase()) > -1;

export default function Selector(props) {
  const [airport, setAirport] = useState("");

  const [filter, setFilter] = useState("");

  const airports = props.airports

  const filteredAirports = useMemo(
    () => airports.filter((airport) => containsText(airport.key, filter) || containsText(airport.label, filter)),
    [filter, airports]
  );

  return (
    <Box>
      <FormControl fullWidth color="success" >
        <InputLabel color="success" id="search-select-label">{props.label}</InputLabel>
        <Select
          labelId="search-select-label"
          id="search-select"
          label={props.label}
          onChange={(e) => {
            let airport = filteredAirports.find(a => a.label === e.target.value)
            setAirport(airport.label)
            props.handleSelect(airport.key)
          }}
          onClose={() => setFilter("")}
          color="success"
          MenuProps={MenuProps}
          value={airport}
        >
          <ListSubheader>
            <TextField
              size="small"
              autoFocus
              placeholder="Type to search..."
              fullWidth
              color="success"
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
            <MenuItem key={airport.key} value={airport.label} color="success" >
              {airport.label}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
  );
}
