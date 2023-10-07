from pydantic import BaseModel, Field


class ReservationSchema(BaseModel):
    labSpaceId: str = Field(...)
    userId: str = Field(...)
    full_name: str = Field(...)
    identification_number: str = Field(...)
    email: str = Field(...)
    phone_number: str = Field(...)
    eafit_affiliation: str = Field(...)
    reservation_date: str = Field(...)
    reservation_time: str = Field(...)
    estimated_duration: int = Field(...)
    number_of_people: int = Field(...)
    additional_services: str = Field(...)
    accepted_terms: bool = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "labSpaceId": "1234567890",
                "userId": "1234567890",
                "full_name": "John Doe",
                "identification_number": "12345678",
                "email": "john.doe@example.com",
                "phone_number": "3001234567",
                "eafit_affiliation": "Estudiante",
                "reservation_date": "2023-10-01",
                "reservation_time": "15:00",
                "estimated_duration": 60,
                "number_of_people": 2,
                "additional_services": "Televisor",
                "accepted_terms": True
            }
        }


class UpdateReservationModel(BaseModel):
    # You can make fields optional for updates, or keep them all as is. This is just an example.
    full_name: str = Field(...)
    email: str = Field(...)
    phone_number: str = Field(...)
    reservation_date: str = Field(...)
    reservation_time: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "full_name": "Jane Doe",
                "email": "jane.doe@example.com",
                "phone_number": "3109876543",
                "reservation_date": "2023-10-02",
                "reservation_time": "14:00"
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
