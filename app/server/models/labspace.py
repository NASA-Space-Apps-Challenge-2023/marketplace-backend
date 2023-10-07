from pydantic import BaseModel, Field


class LabSpaceSchema(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    imgSrc: str = Field(...)
    altText: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Physics Lab",
                "description": "A lab for advanced physics experiments.",
                "imgSrc": "http://localhost:8000/static/images/PhysicsLab.png",
                "altText": "Image of Physics Lab"
            }
        }


class UpdateLabSpaceModel(BaseModel):
    title: str = Field(...)
    description: str = Field(...)
    imgSrc: str = Field(...)
    altText: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "title": "Biology Lab",
                "description": "A lab for biology research.",
                "imgSrc": "http://localhost:8000/static/images/BiologyLab.png",
                "altText": "Image of Biology Lab"
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
