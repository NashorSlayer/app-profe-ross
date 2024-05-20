from fastapi import APIRouter, Depends, HTTPException

from schemas.user import User
from utils.crud.user import get_users, create_user,get_user_by_email
from sqlalchemy.orm import Session
from config.db import get_db

user = APIRouter()
user_path = '/user/'
create_user_path = '/user/create/'


@user.get(user_path ,response_model=list[User])
def get_users_route(db:Session = Depends(get_db)):
    users = get_users(db)
    return users

@user.post(create_user_path, response_model=User)
def create_user_route(user: User, db:Session = Depends(get_db)):
    db_user = get_user_by_email(user.email, db)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(user, db)


