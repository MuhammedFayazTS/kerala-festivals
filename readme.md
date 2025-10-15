# Kerala Festival JSON Repository

![GitHub repo size](https://img.shields.io/github/repo-size/MuhammedFayazTS/kerala-festivals?label=Repo%20Size)
![GitHub last commit](https://img.shields.io/github/last-commit/MuhammedFayazTS/kerala-festivals?color=blue&label=Last%20Update)
![GitHub License](https://img.shields.io/github/license/MuhammedFayazTS/kerala-festivals)
![GitHub stars](https://img.shields.io/github/stars/MuhammedFayazTS/kerala-festivals?style=social)

[![View JSON](https://img.shields.io/badge/View-Festivals.json-green?logo=json&logoColor=white)](https://raw.githubusercontent.com/MuhammedFayazTS/kerala-festivals/main/festivals.json)
[![GitHub Pages](https://img.shields.io/badge/Live%20View-GitHub%20Pages-blue?logo=github)](https://MuhammedFayazTS.github.io/kerala-festivals/festivals.json)

This repository provides structured JSON data for **festivals in Kerala**.  
The data is extracted and cleaned from the official [Kerala Tourism Festival Calendar](https://www.keralatourism.org).

Official [**PDF File**](https://www.keralatourism.org/ebrochures/digital-event-calendar/76)

## Data Structure

Each festival is stored in the following format:

```json
{
  "id": 1,
  "name": "Thrissur Pooram",
  "malayalamName": "ത്രിശ്ശൂർ പൂരം",
  "startDate": "2025-04-23",
  "endDate": "2025-04-23",
  "malayalamDate": "Medam 10, 1200",
  "isMajor": true,
  "location": {
    "district": "Thrissur",
    "place": "Vadakkunnathan Temple, Thrissur",
    "coordinates": {
      "latitude": 10.5276,
      "longitude": 76.2144
    }
  },
  "description": "One of the biggest temple festivals in Kerala, featuring decorated elephants, percussion ensembles, and fireworks.",
  "images": [
    "https://example.com/thrissur-pooram1.jpg",
    "https://example.com/thrissur-pooram2.jpg"
  ],
  "tags": ["Temple Festival", "Pooram", "Cultural"]
}
```

- Date format : `YYYY-MM-DD` (if no `DD` then the date is not decided)

## Usage

You can directly fetch the JSON file in your project:

```js
fetch(
  "https://raw.githubusercontent.com/MuhammedFayazTS/kerala-festivals/main/festivals.json"
)
  .then((res) => res.json())
  .then((data) => console.log(data.festivals));
```

This makes it easier to **integrate into maps, calendars, and apps** without bundling the entire dataset in your frontend.

## Source

Data is taken from the **official Kerala Tourism Event Calendar**:
[https://www.keralatourism.org/](https://www.keralatourism.org)

## Data Extraction

The festival data was extracted from the official Kerala Tourism PDF using the following Python script:

[**dataExtractor.py**](./dataExtractor.py)

Later, the raw JSON was formatted and cleaned with ChatGPT.

Geographical coordinates were then automatically added using:

[**fill_coordinates.py**](./fill_coordinates.py)

remaining empty coordinates where added manually.

[**update_festival_coordinates.py**](./update_festival_coordinates.py)
- used to replace the coordinates in festivals.json

## Disclaimer

> In Kerala, festival dates are decided in accordance with the Malayalam calendar and the local traditions and customs.
> We have given the festival dates based on these. But there can be changes as per the customs and rituals associated with each place of worship.
> As such, these should be considered **indicative only**.

## Contributing

If you notice missing festivals, corrections, or want to improve tags, feel free to open a **pull request** or raise an **issue**.

---

### License

This project is for **educational and cultural purposes**. Data credit: [Kerala Tourism](https://www.keralatourism.org/).
