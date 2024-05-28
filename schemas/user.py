#de fastapi importamos BaseModel
from pydantic import BaseModel,Field, EmailStr


#creamos la clase User que hereda de BaseModel
class User(BaseModel):
    id: int | None = None
    email: EmailStr
    name: str
    last_name: str
    password: str

    class Config:
        from_attributes = True


class UserUpdate(User):
    email: EmailStr | None = None
    name: str | None = None
    last_name: str | None = None
    password: str | None = None
    