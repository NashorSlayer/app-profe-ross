
from pydantic import BaseModel#de fastapi importamos BaseModel


#creamos la clase User que hereda de BaseModel
class User(BaseModel):
    id: int | None = None
    email: str
    name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True


class UserUpdate(User):
    email: str | None = None
    name: str | None = None
    last_name: str | None = None
    password: str | None = None
    