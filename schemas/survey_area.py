from pydantic import BaseModel
from schemas.survey import Survey
from schemas.area import Area


class Survey (BaseModel):
    survey_area_id: int | None = None
    Survey: Survey
    Area: Area