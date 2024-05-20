from pydantic import BaseModel
from schemas.survey import Survey
from schemas.area import Area


class Survey (BaseModel):
    id: int | None = None
    Survey: Survey
    Area: Area

    class Config:
        orm_mode = True