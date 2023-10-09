from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.database.discussion import (
    add_discussion,
    retrieve_discussions,
)
from server.models.discussion import (
    DiscussionSchema,
    ResponseModel,
    ErrorResponseModel,
)

router = APIRouter()


@router.post("/", response_description="Discussion data added into the database")
async def add_discussion_data(discussion: DiscussionSchema = Body(...)):
    discussion = jsonable_encoder(discussion)
    new_discussion = await add_discussion(discussion)
    return ResponseModel(new_discussion, "Discussion added successfully.")

# * Add retrieve_discussions_by_project_id()


@router.get("/", response_description="Discussions retrieved")
async def get_discussions():
    discussions = await retrieve_discussions()
    if discussions:
        return ResponseModel(discussions, "Discussion data retrieved successfully")
    return ResponseModel(discussions, "Empty list returned")
