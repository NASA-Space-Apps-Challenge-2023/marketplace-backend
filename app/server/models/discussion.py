from pydantic import BaseModel, Field


class DiscussionSchema(BaseModel):
    commenter_id: str = Field(...)
    project_id: str = Field(...)
    comment: str = Field(...)
    date_posted: str = Field(...)
    likes: int = Field(0)

    class Config:
        schema_extra = {
            "example": {
                "commenter_id": "user123",
                "project_id": "project123",
                "comment": "This is a sample comment for the project.",
                "date_posted": "2023-10-04",
                "likes": 5
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
