from sqlalchemy.orm import Session

from schemas.user import User
from models.user import User as ModelUser


from cryptography.fernet import Fernet # permite generar una funcion pa cifrar

key = Fernet.generate_key() #genera una clave para cifrar
f = Fernet(key) #cifra la clave

def get_users(db: Session):
    return db.query(ModelUser).all()

def get_user_by_email(email: str, db: Session):
    return db.query(ModelUser).filter(ModelUser.email == email).first()

def create_user(user: User, db: Session):
    user.password = f.encrypt(user.password.encode())
    user = ModelUser(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
