from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from server.database.project import (
    add_project,
    delete_project,
    retrieve_project,
    retrieve_projects,
    update_project,
)
from server.models.project import (
    ErrorResponseModel,
    ResponseModel,
    ProjectSchema,
    UpdateProjectModel,
)

router = APIRouter()


@router.post("/", response_description="Project data added into the database")
async def add_project_data(project: ProjectSchema = Body(...)):
    project = jsonable_encoder(project)
    new_project = await add_project(project)
    return ResponseModel(new_project, "Project added successfully.")


@router.get("/", response_description="Projects retrieved")
async def get_projects():
    projects = await retrieve_projects()
    if projects:
        return ResponseModel(projects, "Project data retrieved successfully")
    return ResponseModel(projects, "Empty list returned")


@router.get("/{id}", response_description="Project data retrieved")
async def get_project_data(id: str):
    project = await retrieve_project(id)
    if project:
        return ResponseModel(project, "Project data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Project doesn't exist.")


@router.put("/{id}", response_description="Project data updated in the database")
async def update_project_data(id: str, req: UpdateProjectModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_project = await update_project(id, req)
    if updated_project:
        return ResponseModel(
            "Project with ID: {} update is successful".format(id),
            "Project data updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the Project data.",
    )


@router.delete("/{id}", response_description="Project data deleted from the database")
async def delete_project_data(id: str):
    deleted_project = await delete_project(id)
    if deleted_project:
        return ResponseModel(
            "Project with ID: {} removed".format(id),
            "Project deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Project with id {0} doesn't exist".format(
            id)
    )
