from .config import database
from bson.objectid import ObjectId

discussion_collection = database.get_collection("discussion_collection")


def discussion_helper(discussion) -> dict:
    return {
        "id": str(discussion["_id"]),
        "commenter_id": discussion["commenter_id"],
        "project_id": discussion["project_id"],
        "comment": discussion["comment"],
        "date_posted": discussion["date_posted"],
        "likes": discussion["likes"]
    }


async def retrieve_discussions():
    discussions = []
    async for discussion in discussion_collection.find():
        discussions.append(discussion_helper(discussion))
    return discussions

# * Add retrieve_discussions_by_project_id()


async def add_discussion(discussion_data: dict) -> dict:
    discussion = await discussion_collection.insert_one(discussion_data)
    new_discussion = await discussion_collection.find_one({"_id": discussion.inserted_id})
    return discussion_helper(new_discussion)
