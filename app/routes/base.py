from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.base import SessionLocal
from app.db import models
from app.schemas.user import UserOut  # ← Tambahkan baris ini

router = APIRouter()

# Dependency untuk akses database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def root():
    return {"message": "Welcome to Public API!"}

@router.get("/ping")
def ping():
    return {"status": "ok"}

@router.get("/users", response_model=list[UserOut])  # ← endpoint baru
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()
