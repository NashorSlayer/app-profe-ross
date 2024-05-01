from fastapi import APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT

from config.db import conn
from schemas.user import User
from models.user import users


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
    return conn.execute(User.select().where(User.c.id==id)).first()

@user.post(ruta_user)
def create_user(user:User):
    new_user = {"email":user.email,"name":user.name,"last_name":user.last_name}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    result = conn.execute(User.insert().values(new_user))
    print(result)
    return "hola mundo"

@user.delete(ruta_user+"/{user_id}")
def delete_user(user_id:int):
    conn.execute(User.delete().where(User.c.id==user_id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put(ruta_user+"/{user_id}")
def update_user(user_id:int,user:User):
    new_user = {"email":user.email,"name":user.name,"last_name":user.last_name}
    new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    conn.execute(User.update().values(new_user).where(User.c.id==user_id))
    return conn.execute(User.select().where(User.c.id==user_id)).first()