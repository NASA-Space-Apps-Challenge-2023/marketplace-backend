from fastapi import APIRouter, Body, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from server.database.reservation import (
    add_reservation,
    delete_reservation,
    retrieve_reservation,
    retrieve_reservations,
    retrieve_reservations_by_user,
    update_reservation,
)

from server.models.reservation import (
    ErrorResponseModel,
    ResponseModel,
    ReservationSchema,
    UpdateReservationModel,
)
from server.dependencies import get_current_user

router = APIRouter()


@router.post("/", response_description="Reservation data added into the database")
async def add_reservation_data(reservation: ReservationSchema = Body(...), current_user: dict = Depends(get_current_user)):
    reservation = jsonable_encoder(reservation)
    new_reservation = await add_reservation(reservation)
    return ResponseModel(new_reservation, "Reservation added successfully.")


@router.get("/", response_description="Reservations retrieved")
async def get_reservations(current_user: dict = Depends(get_current_user)):
    reservations = await retrieve_reservations()
    if reservations:
        return ResponseModel(reservations, "Reservations data retrieved successfully")
    return ResponseModel(reservations, "Empty list returned")


@router.get("/{id}", response_description="Reservation data retrieved")
async def get_reservation_data(id: str, current_user: dict = Depends(get_current_user)):
    reservation = await retrieve_reservation(id)
    if reservation:
        return ResponseModel(reservation, "Reservation data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Reservation doesn't exist.")


@router.put("/{id}", response_description="Reservation data updated in the database")
async def update_reservation_data(id: str, req: UpdateReservationModel = Body(...), current_user: dict = Depends(get_current_user)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_reservation = await update_reservation(id, req)
    if updated_reservation:
        return ResponseModel(
            "Reservation with ID: {} update is successful".format(id),
            "Reservation data updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the reservation data.",
    )


@router.delete("/{id}", response_description="Reservation data deleted from the database")
async def delete_reservation_data(id: str, current_user: dict = Depends(get_current_user)):
    deleted_reservation = await delete_reservation(id)
    if deleted_reservation:
        return ResponseModel(
            "Reservation with ID: {} removed".format(id),
            "Reservation deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Reservation with id {0} doesn't exist".format(
            id)
    )


@router.get("/user/{user_id}", response_description="Reservations retrieved for a specific user")
async def get_reservations_by_user(user_id: str, current_user: dict = Depends(get_current_user)):
    reservations = await retrieve_reservations_by_user(user_id)
    if reservations:
        return ResponseModel(reservations, "Reservations data retrieved successfully")
    return ResponseModel(reservations, "Empty list returned")
