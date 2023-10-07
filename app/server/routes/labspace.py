from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from server.database.labspace import (
    add_labspace,
    delete_labspace,
    retrieve_labspace,
    retrieve_labspaces,
    update_labspace,
)

from server.models.labspace import (
    ErrorResponseModel,
    ResponseModel,
    LabSpaceSchema,
    UpdateLabSpaceModel,
)
from server.dependencies import get_current_user

router = APIRouter()


@router.post("/", response_description="LabSpace data added into the database")
async def add_labspace_data(labspace: LabSpaceSchema = Body(...)):
    labspace = jsonable_encoder(labspace)
    new_labspace = await add_labspace(labspace)
    return ResponseModel(new_labspace, "LabSpace added successfully.")


@router.get("/", response_description="LabSpaces retrieved")
async def get_labspaces():
    labspaces = await retrieve_labspaces()
    if labspaces:
        return ResponseModel(labspaces, "LabSpaces data retrieved successfully")
    return ResponseModel(labspaces, "Empty list returned")


@router.get("/{id}", response_description="LabSpace data retrieved")
async def get_labspace_data(id: str):
    labspace = await retrieve_labspace(id)
    if labspace:
        return ResponseModel(labspace, "LabSpace data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "LabSpace doesn't exist.")


@router.put("/{id}", response_description="LabSpace data updated in the database")
async def update_labspace_data(id: str, req: UpdateLabSpaceModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_labspace = await update_labspace(id, req)
    if updated_labspace:
        return ResponseModel(
            "LabSpace with ID: {} update is successful".format(id),
            "LabSpace data updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the LabSpace data.",
    )


@router.delete("/{id}", response_description="LabSpace data deleted from the database")
async def delete_labspace_data(id: str):
    deleted_labspace = await delete_labspace(id)
    if deleted_labspace:
        return ResponseModel(
            "LabSpace with ID: {} removed".format(id),
            "LabSpace deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "LabSpace with id {0} doesn't exist".format(
            id)
    )
