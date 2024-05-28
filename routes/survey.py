from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import get_db
from utils.crud.survey import (
    get_surveys,
    get_survey_by_id, 
    create_survey, 
    update_survey,        
    delete_survey
)
from schemas.survey import Survey as schema_survey

survey = APIRouter(
    tags=['survey']
)

survey_path = '/survey'
survey_create_path = survey_path +'/create/'
survey_update_path = survey_path +'/update/{survey_id}/'
survey_delete_path = survey_path +'/delete/{survey_id}/' 

#messages
survey_not_found = 'survey not found'
survey_already_registered = 'survey already registered'

@survey.get(survey_path)
def get_surveys_route(db:Session = Depends(get_db)):
    return get_surveys(db)

@survey.post(survey_create_path, response_model=schema_survey)
def create_survey_route(survey: schema_survey, db:Session = Depends(get_db)):
    return create_survey(survey, db)

@survey.patch(survey_update_path)
def update_survey_route(survey_id: int, survey: schema_survey, db:Session = Depends(get_db)):
    survey_db = get_survey_by_id(survey_id, db)
    if survey_db == None:
        raise HTTPException(status_code=404, detail='Survey not found')
    return update_survey(survey_id, survey, db)

@survey.delete(survey_delete_path)
def delete_survey_route(survey_id: int, db:Session = Depends(get_db)):
    survey_db = get_survey_by_id(survey_id, db)
    if survey_db == None:
        raise HTTPException(status_code=404, detail='Survey not found')
    return delete_survey(survey_id, db)

