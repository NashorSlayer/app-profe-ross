from pydantic import BaseModel

class Survey (BaseModel):
    survey_id: int | None = None
    name: str
    description: str
    time_range_init: str
    time_range_end: str
    answer_time_init: str
    answer_time_end: str
    user_id: int