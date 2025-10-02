import pdfplumber
import json
import re

def extract_festivals_from_pdf(pdf_path, output_json):
    festivals = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, start=2):

            text = page.extract_text()
            if not text:
                continue

            # Split text lines
            lines = [line.strip() for line in text.split("\n") if line.strip()]

            if len(lines) < 5:
                # Skip if not enough content
                continue

            # Mapping based on your structure
            raw_date = lines[0]
            raw_name = lines[1]
            raw_year = lines[2]
            raw_location = lines[3]
            description_lines = lines[4:-1]  # Skip last line
            description = " ".join(description_lines).strip()

            if raw_name == "S M T W T F S S M T W T F S":
                continue

            festivals.append({
                "date": raw_date,
                "name": raw_name,
                "year": raw_year,
                "location": raw_location,
                "description": description + ".",
                # "page": page_num
            })

    # Save as JSON
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump({"festivals": festivals}, f, indent=2, ensure_ascii=False)

    print(f"✅ Extracted {len(festivals)} festivals into {output_json}")

extract_festivals_from_pdf("input_festival_calender.pdf", "festivals_raw.json")
