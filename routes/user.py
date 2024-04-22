from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User
#users es la tabla que se creo en el archivo models/user.py


user = APIRouter()
ruta_user = "/users"

@user.get(ruta_user)
def get_user():
    return conn.execute(users.select()).fetchall()

@user.post(ruta_user)
def create_user(user:User):
    print(user)
    return "a"