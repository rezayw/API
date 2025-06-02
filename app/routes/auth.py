from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.db.base import SessionLocal
from app.crud.user import get_user_by_email, create_user
from typing import List  # ← untuk response_model bertipe list


router = APIRouter()

# Dependency untuk mendapatkan DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.get("/users", response_model=List[UserOut])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
