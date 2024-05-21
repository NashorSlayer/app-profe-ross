from sqlalchemy.orm import Session

from schemas.user import User as SchemaUser
from models.user import User as ModelUser


from cryptography.fernet import Fernet # permite generar una funcion pa cifrar

key = Fernet.generate_key() #genera una clave para cifrar
f = Fernet(key) #cifra la clave

def get_users(db: Session):
    return db.query(ModelUser).all()

def get_user_by_email(email: str, db: Session):
    return db.query(ModelUser).filter(ModelUser.email == email).first()

def get_user_by_id(user_id: int, db: Session):
    return db.query(ModelUser).filter(ModelUser.id == user_id).first()

def create_user(user: SchemaUser, db: Session):
    user.password = f.encrypt(user.password.encode())
    
    #parsing info to ModelUser
    db_user = ModelUser(
        email=user.email, 
        password=user.password,
        name=user.name,
        last_name=user.last_name
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(user_id: int, user: SchemaUser, db: Session):
    db_user = db.query(ModelUser).filter(ModelUser.id == user_id).first()
    if user.password != None:
        print(user.password)
        user.password = f.encrypt(user.password.encode())
        db_user.password = user.password
    if user.email != None:
        db_user.email = user.email
    if user.name != None:
        db_user.name = user.name
    if user.last_name != None:
        db_user.last_name = user.last_name
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(user_id: int, db: Session):
    db_user = db.query(ModelUser).filter(ModelUser.id == user_id).first()
    db.delete(db_user)
    db.commit()
    return 'User deleted'