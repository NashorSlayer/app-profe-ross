from pydantic import BaseModel
from schemas.survey import Survey
from schemas.area import Area


class Survey_areas (BaseModel):
    id: int | None = None
    Survey: Survey
    Area: Area

    class Config:
        from_attributes = True