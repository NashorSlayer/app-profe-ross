from fastapi import FastAPI

from routes.user import user
from routes.area import area
from utils.constants import (
    users,
    users_description,
    areas,
    areas_description
    )

app = FastAPI(
    title= "API FastAPI de proyecto con profesor Eric Ross",
    description=" descripcion de prueba",
    version="1.0.0",
    openapi_tags=[{
        "name": users,
        "description": users_description
    },
    {
        "name": areas,
        "description": areas_description,
    }]
)
app.include_router(user)
app.include_router(area)
