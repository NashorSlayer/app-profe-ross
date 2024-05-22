from fastapi import APIRouter, Depends, HTTPException

from schemas.user import User,UserUpdate
from utils.crud.user import (
    get_users,
    create_user,
    get_user_by_email, 
    get_user_by_id,
    update_user,
    delete_user
    )
from sqlalchemy.orm import Session
from config.db import get_db

user = APIRouter(
    tags=['users']
)
user_path = '/user/'
create_user_path = '/user/create/'
patch_user_path = '/user/update/{user_id}/'
delete_user_path = '/user/delete/{user_id}/'


#messages
user_not_found = 'User not found'
user_already_registered = 'Email already registered'


@user.get(user_path ,response_model=list[User])
def get_users_route(db:Session = Depends(get_db)):
    users = get_users(db)
    return users

@user.post(create_user_path, response_model=User)
def create_user_route(user: User, db:Session = Depends(get_db)):
    db_user = get_user_by_email(user.email, db)
    if db_user:
        raise HTTPException(status_code=400, detail=user_already_registered)
    return create_user(user, db)

@user.patch(patch_user_path, response_model=User)
def update_user_route(user_id: int, user:UserUpdate, db:Session = Depends(get_db)):
    db_user = get_user_by_id(user_id, db)
    if db_user == None:
        raise HTTPException(status_code=404, detail=user_not_found)
    return update_user(user_id, user, db)

@user.delete(delete_user_path, status_code=200)
def delete_user_route(user_id: int, db:Session = Depends(get_db)):
    db_user = get_user_by_id(user_id, db)
    if db_user == None:
        raise HTTPException(status_code=404, detail=user_not_found)
    message = delete_user(user_id,db)
    return {'message': message}