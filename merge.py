"""
Merge all transformed records into the final output files.

Produces:
- output/services.csv — the full dataset as CSV
- output/services.json — the full dataset as JSON
- output/SOURCES.md — attribution for all data sources used
"""

import csv
import json
import os
from datetime import date
from config import SOURCES, SCHEMA_FIELDS
from transform import main as transform_all


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")


def write_csv(records, path):
    """Write records to a CSV file."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA_FIELDS)
        writer.writeheader()
        for record in records:
            # Ensure all fields exist
            row = {field: record.get(field, "") for field in SCHEMA_FIELDS}
            writer.writerow(row)
    print(f"  Written: {path} ({len(records)} records)")


def write_json(records, path):
    """Write records to a JSON file."""
    output = []
    for record in records:
        row = {field: record.get(field, "") for field in SCHEMA_FIELDS}
        output.append(row)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Written: {path} ({len(records)} records)")


def write_sources(path):
    """Write attribution file for all data sources."""
    today = date.today().strftime("%d %B %Y")

    lines = [
        "# Data Sources and Attribution",
        "",
        "All data in this repository is sourced from Australian government open data portals.",
        "Each dataset is used under its respective Creative Commons license.",
        "",
        "## Attribution",
        "",
        "As required by data.gov.au:",
        "",
    ]

    for source in SOURCES:
        lines.append(f"- **{source['organisation']}**, {source['jurisdiction']}, "
                      f"*{source['name']}*, Sourced on {today}, "
                      f"[Dataset URL]({source['dataset_url']}). "
                      f"License: {source['license']}")

    lines.append("")
    lines.append(f"Last updated: {date.today().isoformat()}")
    lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"  Written: {path}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Running transform...")
    records = transform_all()

    if not records:
        print("No records to output.")
        return

    print(f"\nWriting output ({len(records)} total records)...")
    write_csv(records, os.path.join(OUTPUT_DIR, "services.csv"))
    write_json(records, os.path.join(OUTPUT_DIR, "services.json"))
    write_sources(os.path.join(OUTPUT_DIR, "SOURCES.md"))

    print("\nDone.")


if __name__ == "__main__":
    main()
