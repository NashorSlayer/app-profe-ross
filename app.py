from fastapi import FastAPI, Depends, HTTPException
from config.db import Session_local
from sqlalchemy.orm import Session
from schemas.user import User
from utils.crud.user import get_users

app = FastAPI()

#Dependency
def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()

@app.get('/user/' ,response_model=list[User])
def get_users_route(db:Session = Depends(get_db)):
    users = get_users(db)
    return users