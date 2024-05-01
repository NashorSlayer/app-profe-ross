
from pydantic import BaseModel #de fastapi importamos BaseModel

#creamos la clase User que hereda de BaseModel
class User(BaseModel):
    user_id: int | None = None
    email: str
    name: str
    last_name: str
    password:str