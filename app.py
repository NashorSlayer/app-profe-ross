from fastapi import FastAPI

from routes.user import user as user_routes
from routes.area import area as area_routes
from routes.survey import survey as survey_routes


from utils.constants import (
    users,
    users_description,
    areas,
    areas_description,
    survey,
    survey_description,
    survey_area,
    survey_area_description,
    survey_answer,
    survey_answer_description
    )

app = FastAPI(
    title= "API FastAPI de proyecto con profesor Eric Ross",
    description=" descripcion de prueba",
    version="0.1.0",
    openapi_tags=[{
        "name": users,
        "description": users_description
    },
    {
        "name": areas,
        "description": areas_description,
    },{
        "name":survey,
        "description":survey_description
    }]
)

app.include_router(user_routes)
app.include_router(area_routes)
app.include_router(survey_routes)
