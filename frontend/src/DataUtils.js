export default class Airport {
  constructor(label, key) {
    this.key = key
    this.label = label
  }

  static allAirports() { //TODO
    return [
      new Airport("Kraków Balice", "KRK"),
      new Airport("Warszawa Okęcie", "WAW"),
      new Airport("London Stansted", "LST")
    ]
  }
}