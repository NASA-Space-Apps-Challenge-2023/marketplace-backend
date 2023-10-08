import pandas as pd
import random
from pymongo import MongoClient
from app.server.models.project import ProjectSchema
from typing import List
from decouple import config

MONGO_URL = config(
    'MONGO_URL',
    default="mongodb://root:examplepassword@localhost:27017/?authMechanism=DEFAULT"
)

print(MONGO_URL)

# Load CSV data
df = pd.read_csv("./feed.csv")

# Establish MongoDB Connection
try:
    conn = MongoClient(MONGO_URL)
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# Connect to the database and collection
db = conn.scicollab
collection = db.project_collection


def transform_row_to_schema(row) -> dict:
    """Transform a row to follow the ProjectSchema format."""
    try:
        data = {
            "project_name": row.get("project_name", ""),
            "project_url_on_catalog": row.get("project_url_on_catalog", ""),
            "project_url_external": row.get("project_url_external", ""),
            "project_description": row.get("project_description", ""),
            "keywords": str(row.get("keywords", "")).split(", "),
            "fields_of_science": str(row.get("fields_of_science", "")).split(", "),
            "project_status": row.get("project_status", ""),
            "agency_sponsor": row.get("agency_sponsor", ""),
            "agency_sponsor_other": row.get("agency_sponsor_other", "N/A"),
            "gov_contact": row.get("gov_contact", ""),
            "gov_contact_email": row.get("gov_contact_email", ""),
            "geographic_scope": row.get("geographic_scope", ""),
            "participant_age": row.get("participant_age", ""),
            "participation_tasks": str(row.get("participation_tasks", "")).split(", "),
            "scistarter": row.get("scistarter", ""),
            "email": row.get("email", "no-email@example.com"),
            "start_date": row.get("start_date", ""),
            "project_goals": row.get("project_goals", "Change the world"),
            "stars": random.randint(0, 5),
            "collaborators": row.get("collaborators", []),
            "owner_id": "6522da15712e447ae02b61f5",
            "discussions": row.get("discussions", [])
        }
        return data
    except Exception as e:
        print(f"Error: {e} for row: {row}")
        return None


def validate_data_against_schema(data: List[dict]):
    """Validate data against the project schema."""
    validated_data = []
    for item in data:
        try:
            validated_data.append(ProjectSchema(**item))
        except Exception as e:
            print(f"Data validation error: {e} for data: {item}")
    return validated_data


def migrate_data(validated_data):
    """Insert validated data into MongoDB."""
    for item in validated_data:
        try:
            collection.insert_one(item.dict())
            # ! Uncomment to DEBUG the Inserted data
            # print(f"Inserted data: {item.dict()}")
        except Exception as e:
            print(f"Data insertion error: {e} for data: {item}")


def main():
    transformed_data = [transform_row_to_schema(
        row) for _, row in df.iterrows()]
    # Remove None items
    filtered_data = [item for item in transformed_data if item]
    validated_data = validate_data_against_schema(filtered_data)
    migrate_data(validated_data)


if __name__ == "__main__":
    main()
