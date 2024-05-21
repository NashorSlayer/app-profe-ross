
from pydantic import BaseModel

class Area (BaseModel):
    id: int | None = None
    name: str

    class Config:
        orm_mode = True
        