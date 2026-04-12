# commons-au pipeline

Automated ETL pipeline that fetches open data from Australian government portals, standardises it into a common schema, and publishes the result to [commons-au/data](https://github.com/commons-au/data).

## How It Works

```
Government CKAN APIs → fetch.py → sources/ (raw CSVs)
                                      ↓
                                transform.py → standardised records
                                      ↓
                                  merge.py → output/services.csv + services.json
                                      ↓
                              GitHub Actions → pushes to commons-au/data
```

## Data Sources

All data is fetched from Australian government open data portals via their public CKAN APIs. See [commons-au/landscape](https://github.com/commons-au/landscape) for full documentation of these portals.

| Portal | API Base URL |
|--------|-------------|
| Federal (data.gov.au) | `https://data.gov.au/data/api/3/action/` |
| NSW | `https://data.nsw.gov.au/data/api/3/action/` |
| VIC | `https://discover.data.vic.gov.au/api/3/action/` |
| QLD | `https://www.data.qld.gov.au/api/3/action/` |
| SA | `https://data.sa.gov.au/data/api/3/action/` |
| WA | `https://catalogue.data.wa.gov.au/api/3/action/` |

## Running Locally

```bash
pip install -r requirements.txt

python fetch.py        # Download raw data from government APIs
python transform.py    # Clean and standardise into common schema
python merge.py        # Combine into services.csv and services.json
```

Output will be in the `output/` directory.

## Automation

The pipeline runs weekly via GitHub Actions (see `.github/workflows/etl.yml`). Each run:

1. Fetches the latest data from all government portals
2. Cleans and standardises it
3. Commits the result to [commons-au/data](https://github.com/commons-au/data)

## Attribution

All data sourced from Australian government portals is used under Creative Commons Attribution licenses. Full attribution is maintained in the output `SOURCES.md` file, following the format required by data.gov.au:

> Organisation name, jurisdiction, title of dataset, date sourced, dataset URL

## License

This pipeline code is released under [CC0 1.0](LICENSE) — public domain, no restrictions.
