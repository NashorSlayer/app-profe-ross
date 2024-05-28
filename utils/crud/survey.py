from sqlalchemy.orm import Session
from schemas.survey import Survey as schema_survey
from models.survey import Survey as models_survey
from .user import get_user_by_id

def get_surveys(db: Session):
    return db.query(models_survey).limit(10).all()

def get_survey_by_id(survey_id: int, db: Session):
    return db.query(models_survey).filter(models_survey.id == survey_id).first()

def get_survey_by_name(name: str, db: Session):
    return db.query(models_survey).filter(models_survey.name == name).first()

def create_survey(survey: schema_survey, db: Session):
    if get_user_by_id(survey.User.id, db):
        return {'error': 'User not found', "status": 404}
    db_survey = models_survey(
        name=survey.name,
        description=survey.description,
        time_range_start=survey.time_range_start,
        time_range_end=survey.time_range_end,
        time_answer_start=survey.time_answer_start,
        time_answer_end=survey.time_answer_end,
        user_id=survey.user_id
    )
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def update_survey(survey_id: int, survey: schema_survey, db: Session):
    db_survey = db.query(models_survey).filter(models_survey.id == survey_id).first()
    if survey.name != None:
        db_survey.name = survey.name
    if survey.description != None:
        db_survey.description = survey.description
    if survey.time_range_start != None:
        db_survey.time_range_start = survey.time_range_start
    if survey.time_range_end != None:
        db_survey.time_range_end = survey.time_range_end
    if survey.time_answer_start != None:
        db_survey.time_answer_start = survey.time_answer_start
    if survey.time_answer_end != None:
        db_survey.time_answer_end = survey.time_answer_end
    if survey.user_id != None:
        db_survey.user_id = survey.user_id
    db.commit()
    db.refresh(db_survey)
    return db_survey

def delete_survey(survey_id: int, db: Session):
    db_survey = db.query(models_survey).filter(models_survey.id == survey_id).first()
    db.delete(db_survey)
    db.commit()
    return 'Survey deleted'

