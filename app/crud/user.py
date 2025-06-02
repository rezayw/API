from sqlalchemy.orm import Session
from app.db import models
from app.schemas.user import UserCreate
import hashlib

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: UserCreate):
    hashed_pw = hashlib.sha256(user.password.encode()).hexdigest()
    db_user = models.User(
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
