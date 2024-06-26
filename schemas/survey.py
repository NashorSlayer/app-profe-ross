from pydantic import BaseModel
from schemas.user import User


class Survey (BaseModel):
    id: int | None = None
    name: str
    description: str
    time_range_init: str
    time_range_end: str
    answer_time_init: str
    answer_time_end: str
    User: User

    class Config:
        from_attributes = True
        