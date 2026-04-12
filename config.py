"""
Data source configuration for the commons-au pipeline.

Each source defines:
- id: unique identifier used for filenames and tracking
- name: human-readable name of the dataset
- organisation: the government agency that publishes it
- jurisdiction: state/territory or "federal"
- url: direct download URL for the CSV
- license: the license identifier
- license_url: link to the license text
- dataset_url: link to the dataset page on the portal
- field_map: mapping from source column names to our schema fields
"""

SCHEMA_FIELDS = [
    "id",
    "name",
    "description",
    "category",
    "address",
    "suburb",
    "state",
    "postcode",
    "latitude",
    "longitude",
    "phone",
    "email",
    "website",
    "hours",
    "eligibility",
    "cost",
    "source_id",
    "source_name",
    "source_organisation",
    "source_jurisdiction",
    "source_license",
    "source_url",
    "source_date",
]

CATEGORIES = {
    # Mapping from various source labels to our standard categories
    "drug and alcohol": "alcohol_drugs",
    "needle exchange": "alcohol_drugs",
    "counselling and psychiatric services": "mental_health",
    "mental health": "mental_health",
    "health services / pharmacy": "health",
    "health services": "health",
    "health": "health",
    "doctor": "health",
    "dental": "health",
    "food": "food",
    "meals": "food",
    "food relief": "food",
    "pantry/groceries": "food",
    "hot meals": "food",
    "accommodation": "housing",
    "housing": "housing",
    "emergency accommodation": "housing",
    "legal": "legal",
    "legal services": "legal",
    "material aid / financial aid": "financial",
    "financial aid": "financial",
    "centrelink": "financial",
    "employment": "employment",
    "education": "education",
    "disability": "disability",
    "family services": "family",
    "domestic violence": "family",
    "recreation": "community",
    "community": "community",
    "information and referral": "information",
    "transport": "transport",
    "technology": "technology",
    "personal care": "personal_care",
}

SOURCES = [
    {
        "id": "vic_melbourne_helping_out",
        "name": "Free and Cheap Support Services (Helping Out)",
        "organisation": "City of Melbourne",
        "jurisdiction": "VIC",
        "url": "https://data.melbourne.vic.gov.au/api/v2/catalog/datasets/free-and-cheap-support-services-with-opening-hours-public-transport-and-parking-/exports/csv?delimiter=%2C",
        "license": "CC-BY-4.0",
        "license_url": "https://creativecommons.org/licenses/by/4.0/",
        "dataset_url": "https://discover.data.vic.gov.au/dataset/free-and-cheap-support-services-with-opening-hours-public-transport-and-parking-options-helping",
        "field_map": {
            "name": "name",
            "description": "what",
            "address": "address_1",
            "suburb": "suburb",
            "phone": "phone",
            "email": "email",
            "website": "website",
            "latitude": "latitude",
            "longitude": "longitude",
            "cost": "cost",
            # Hours are in separate day columns — handled in transform
            "hours_monday": "monday",
            "hours_tuesday": "tuesday",
            "hours_wednesday": "wednesday",
            "hours_thursday": "thursday",
            "hours_friday": "friday",
            "hours_saturday": "saturday",
            "hours_sunday": "sunday",
            # Categories are in separate columns — handled in transform
            "category_1": "category_1",
            "category_2": "category_2",
            "category_3": "category_3",
            "category_4": "category_4",
            "category_5": "category_5",
            "category_6": "category_6",
        },
    },
    {
        "id": "vic_casey_food_relief",
        "name": "Emergency Food Relief Groups",
        "organisation": "City of Casey",
        "jurisdiction": "VIC",
        "url": "https://data.casey.vic.gov.au/api/v2/catalog/datasets/emergency-food-relief-groups/exports/csv?delimiter=%2C",
        "license": "Other (Open)",
        "license_url": "",
        "dataset_url": "https://discover.data.vic.gov.au/dataset/emergency-food-relief-groups",
        "field_map": {
            "name": "provider",
            "description": "service_description",
            "address": "address",
            "suburb": "suburb",
            "postcode": "postcode",
            "phone": "public_telephone_no",
            "email": "email_adress",
            "website": "website",
            "latitude": "latitude",
            "longitude": "longitude",
            "hours_1": "service_hours1",
            "hours_2": "service_hours2",
        },
    },
]
