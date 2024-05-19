from fastapi import APIRouter, Depends

from schemas.user import User
from utils.crud.user import get_users
from sqlalchemy.orm import Session
from config.db import get_db

user = APIRouter()
user_path = '/user/'


@user.get(user_path ,response_model=list[User])
def get_users_route(db:Session = Depends(get_db)):
    users = get_users(db)
    return users