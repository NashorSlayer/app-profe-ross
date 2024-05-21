from sqlalchemy.orm import Session
from schemas.area import Area as SchemaArea
from models.area import Area as ModelArea

def get_areas(db: Session):
    return db.query(ModelArea).limit(10).all() 

def get_area_by_id(area_id: int, db: Session):
    return db.query(ModelArea).filter(ModelArea.id == area_id).first()

def get_area_by_name(name: str, db: Session):
    return db.query(ModelArea).filter(ModelArea.name == name).first()

def create_area(area: SchemaArea, db: Session):
    db_area = ModelArea(
        name=area.name
    )
    db.add(db_area)
    db.commit()
    db.refresh(db_area)
    return db_area

def update_area(area_id: int, area: SchemaArea, db: Session):
    db_area = db.query(ModelArea).filter(ModelArea.id == area_id).first()
    if area.name != None:
        db_area.name = area.name
    db.commit()
    db.refresh(db_area)
    return db_area

def delete_area(area_id: int, db: Session):
    db_area = db.query(ModelArea).filter(ModelArea.id == area_id).first()
    db.delete(db_area)
    db.commit()
    return 'Area deleted'