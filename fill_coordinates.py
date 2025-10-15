import json
import time
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable

INPUT_FILE = "festivals.json"
OUTPUT_FILE = "./data/festivals_with_coordinates.json"

# Initialize geolocator
geolocator = Nominatim(user_agent="festival-coord-filler")

def get_coordinates(place_name):
    """Fetch coordinates for a place using Nominatim with retry."""
    try:
        location = geolocator.geocode(place_name)
        if location:
            return {"latitude": location.latitude, "longitude": location.longitude}
    except (GeocoderTimedOut, GeocoderUnavailable):
        time.sleep(2)
        return get_coordinates(place_name)
    return {"latitude": None, "longitude": None}

def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        input_data = json.load(f)

    data = input_data.get("festivals", input_data)

    names_array = [
        {
            "name": item["name"],
            "id": item["id"],
            "location": item["location"],
        }
        for item in data
    ]

    total = len(names_array)
    
    print(f"Total places: {total}\n")

    for index, item in enumerate(names_array, start=1):
        place_name = item["location"]["place"]
        print(f"\n[{index}/{total}] Fetching coordinates for: {place_name}...")

        coords = get_coordinates(place_name)
        item["location"]["coordinates"] = coords

        print(f" → {coords}")
        remaining = total - index
        print(f"Remaining: {remaining} item{'s' if remaining != 1 else ''}")
        time.sleep(1)

    output = {"festivals": names_array}

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"✅ Coordinates added successfully! Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
