from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from models.user import users #users es la tabla que se creo en el archivo models/user.py
from schemas.user import User


from cryptography.fernet import Fernet # permite generar una funcion pa cifrar

key = Fernet.generate_key() #genera una clave para cifrar
f = Fernet(key) #cifra la clave

user = APIRouter()
ruta_user = "/users"

@user.get(ruta_user)
def get_user():
    return conn.execute(users.select()).fetchall()

@user.get(ruta_user+"/{user_id}")
def get_user(id: int):
    return conn.execute(users.select().where(users.c.id==id)).first()

@user.post(ruta_user)
def create_user(user:User):
    new_user = {"email":user.email,"name":user.name,"last_name":user.last_name}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(user.insert().values(new_user))
    return conn.execute(user.select().where(user.c.id==result.lastrowid)).first()

@user.delete(ruta_user+"/{user_id}")
def delete_user(user_id:int):
    conn.execute(users.delete().where(users.c.id==user_id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put(ruta_user+"/{user_id}")
def update_user(user_id:int,user:User):
    new_user = {"email":user.email,"name":user.name,"last_name":user.last_name}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    conn.execute(users.update().values(new_user).where(users.c.id==user_id))
    return conn.execute(users.select().where(users.c.id==user_id)).first()