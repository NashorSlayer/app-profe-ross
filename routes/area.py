from utils.crud.area import (
    get_areas,
    get_area_by_id,
    get_area_by_name, 
    create_area, 
    update_area, 
    delete_area 
)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from schemas.area import Area as SchemaArea


area = APIRouter(
    tags=['areas']
)
area_path = '/area/'
area_create_path = area_path+'create/'
area_update_path = area_path+'update/{area_id}/'
area_delete_path = area_path+'delete/{area_id}/' 


#messages
area_not_found = 'Area not found'
area_already_registered = 'Area already registered'

@area.get(area_path, response_model=list[SchemaArea])
def get_areas_route(db:Session = Depends(get_db)):
    areas = get_areas(db)
    return areas

@area.post(area_create_path, response_model=SchemaArea)
def create_area_route(area: SchemaArea, db:Session = Depends(get_db)):
    db_area = get_area_by_name(area.name, db)
    if db_area:
        raise HTTPException(status_code=400, detail=area_already_registered)
    return create_area(area, db)

@area.patch(area_update_path, response_model=SchemaArea)
def update_area_route(area_id: int, area:SchemaArea, db:Session = Depends(get_db)):
    db_area = get_area_by_id(area_id, db)
    if db_area == None:
        raise HTTPException(status_code=404, detail=area_not_found)
    return update_area(area_id, area, db)

@area.delete(area_delete_path, status_code=200)
def delete_area_route(area_id: int, db:Session = Depends(get_db)):
    db_area = get_area_by_id(area_id, db)
    if db_area == None:
        raise HTTPException(status_code=404, detail=area_not_found)
    message = delete_area(area_id,db)
    return {'message': message}