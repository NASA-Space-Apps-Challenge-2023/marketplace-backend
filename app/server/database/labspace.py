from bson.objectid import ObjectId
from .config import database

labspace_collection = database.get_collection("labspace_collection")


def labspace_helper(labspace) -> dict:
    return {
        "id": str(labspace["_id"]),
        "title": labspace["title"],
        "description": labspace["description"],
        "imgSrc": labspace["imgSrc"],
        "altText": labspace["altText"]
    }


async def retrieve_labspaces():
    labspaces = []
    async for labspace in labspace_collection.find():
        labspaces.append(labspace_helper(labspace))
    return labspaces


async def add_labspace(labspace_data: dict) -> dict:
    labspace = await labspace_collection.insert_one(labspace_data)
    new_labspace = await labspace_collection.find_one({"_id": labspace.inserted_id})
    return labspace_helper(new_labspace)


async def retrieve_labspace(id: str) -> dict:
    labspace = await labspace_collection.find_one({"_id": ObjectId(id)})
    if labspace:
        return labspace_helper(labspace)


async def update_labspace(id: str, data: dict):
    if len(data) < 1:
        return False
    labspace = await labspace_collection.find_one({"_id": ObjectId(id)})
    if labspace:
        updated_labspace = await labspace_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_labspace:
            return True
        return False


async def delete_labspace(id: str):
    labspace = await labspace_collection.find_one({"_id": ObjectId(id)})
    if labspace:
        await labspace_collection.delete_one({"_id": ObjectId(id)})
        return True
