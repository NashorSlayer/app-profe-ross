from pydantic import BaseModel
from schemas.survey import Survey
from schemas.area import Area

class SurveyArea (BaseModel):
    id: int | None = None
    Survey: Survey
    Area: Area
    time: int

    class Config:
        orm_mode = True
        