from bson.objectid import ObjectId
from .config import database

project_collection = database.get_collection("project_collection")


def project_helper(project) -> dict:
    return {
        "id": str(project["_id"]),
        "project_name": project["project_name"],
        "project_url_on_catalog": project.get("project_url_on_catalog", None),
        "project_url_external": project.get("project_url_external", None),
        "project_description": project["project_description"],
        "keywords": project["keywords"],
        "fields_of_science": project["fields_of_science"],
        "project_status": project["project_status"],
        "agency_sponsor": project.get("agency_sponsor", None),
        "agency_sponsor_other": project.get("agency_sponsor_other", None),
        "gov_contact": project.get("gov_contact", None),
        "gov_contact_email": project.get("gov_contact_email", None),
        "geographic_scope": project.get("geographic_scope", None),
        "participant_age": project.get("participant_age", None),
        "participation_tasks": project["participation_tasks"],
        "scistarter": project.get("scistarter", None),
        "email": project["email"],
        "start_date": project["start_date"],
        "project_goals": project.get("project_goals", None),
        "stars": project.get("stars", 0),  # Default to 0 if not provided
        "collaborators": project.get("collaborators", []),
        "owner_id": project["owner_id"],
        "discussions": project.get("discussions", []),
    }


async def retrieve_projects():
    projects = []
    async for project in project_collection.find():
        projects.append(project_helper(project))
    return projects


async def add_project(project_data: dict) -> dict:
    project = await project_collection.insert_one(project_data)
    new_project = await project_collection.find_one({"_id": project.inserted_id})
    return project_helper(new_project)


async def retrieve_project(id: str) -> dict:
    project = await project_collection.find_one({"_id": ObjectId(id)})
    if project:
        return project_helper(project)


async def update_project(id: str, data: dict):
    if len(data) < 1:
        return False
    project = await project_collection.find_one({"_id": ObjectId(id)})
    if project:
        updated_project = await project_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_project:
            return True
        return False


async def delete_project(id: str):
    project = await project_collection.find_one({"_id": ObjectId(id)})
    if project:
        await project_collection.delete_one({"_id": ObjectId(id)})
        return True
