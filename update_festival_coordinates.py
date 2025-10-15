import json
import os

# Input files
MAIN_FILE = "festivals.json"
COORD_FILE = "./data/festivals_with_coordinates.json"
OUTPUT_FILE = "festivals_updated.json"  # safer to not overwrite directly

def main():
    # Load main festival file
    with open(MAIN_FILE, "r", encoding="utf-8") as f:
        main_data = json.load(f)

    # Load coordinates file
    with open(COORD_FILE, "r", encoding="utf-8") as f:
        coord_data = json.load(f)

    main_festivals = main_data.get("festivals", [])
    coord_festivals = coord_data.get("festivals", [])

    # Create a lookup dictionary for faster access by ID
    coord_lookup = {f["id"]: f for f in coord_festivals}

    updated_count = 0
    missing_count = 0

    for fest in main_festivals:
        fid = fest["id"]
        if fid in coord_lookup:
            coord_entry = coord_lookup[fid]
            fest["location"]["place"] = coord_entry["location"]["place"]
            fest["location"]["coordinates"] = coord_entry["location"]["coordinates"]
            updated_count += 1
        else:
            missing_count += 1
            print(f"⚠️ No coordinate entry found for ID {fid}: {fest['name']}")

    # Save to new file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump({"festivals": main_festivals}, f, indent=2, ensure_ascii=False)

    print(f"✅ Update complete!")
    print(f" - Updated {updated_count} records")
    print(f" - Missing {missing_count} records (no match found)")
    print(f"💾 Saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
