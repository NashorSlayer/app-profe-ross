from fastapi import APIRouter

user = APIRouter()
ruta_user = "/users"

@user.get(ruta_user)
def helloworld():
    return {"Hello": "World 2"}
