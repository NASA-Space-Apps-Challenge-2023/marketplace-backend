from bson.objectid import ObjectId
from .config import database

reservation_collection = database.get_collection("reservations_collection")


def reservation_helper(reservation) -> dict:
    return {
        "id": str(reservation["_id"]),
        "labSpaceId": reservation["labSpaceId"],
        "userId": reservation["userId"],
        "full_name": reservation["full_name"],
        "identification_number": reservation["identification_number"],
        "email": reservation["email"],
        "phone_number": reservation["phone_number"],
        "eafit_affiliation": reservation["eafit_affiliation"],
        "reservation_date": reservation["reservation_date"],
        "reservation_time": reservation["reservation_time"],
        "estimated_duration": reservation["estimated_duration"],
        "number_of_people": reservation["number_of_people"],
        "additional_services": reservation["additional_services"],
        "accepted_terms": reservation["accepted_terms"]
    }


async def retrieve_reservations():
    reservations = []
    async for reservation in reservation_collection.find():
        reservations.append(reservation_helper(reservation))
    return reservations


async def add_reservation(reservation_data: dict) -> dict:
    reservation = await reservation_collection.insert_one(reservation_data)
    new_reservation = await reservation_collection.find_one({"_id": reservation.inserted_id})
    return reservation_helper(new_reservation)


async def retrieve_reservation(id: str) -> dict:
    reservation = await reservation_collection.find_one({"_id": ObjectId(id)})
    if reservation:
        return reservation_helper(reservation)


async def update_reservation(id: str, data: dict):
    if len(data) < 1:
        return False
    reservation = await reservation_collection.find_one({"_id": ObjectId(id)})
    if reservation:
        updated_reservation = await reservation_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_reservation:
            return True
        return False


async def delete_reservation(id: str):
    reservation = await reservation_collection.find_one({"_id": ObjectId(id)})
    if reservation:
        await reservation_collection.delete_one({"_id": ObjectId(id)})
        return True


async def retrieve_reservations_by_user(user_id: str):
    reservations = []
    async for reservation in reservation_collection.find({"userId": user_id}):
        reservations.append(reservation_helper(reservation))
    return reservations
