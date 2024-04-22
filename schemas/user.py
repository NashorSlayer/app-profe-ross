
from typing import Optional #importamos Optional para poder definir un campo como opcional
from pydantic import BaseModel #de fastapi importamos BaseModel

#creamos la clase User que hereda de BaseModel
class User(BaseModel):
    user_id: Optional[int]
    email: str
    name: str
    last_name: str
    password:str