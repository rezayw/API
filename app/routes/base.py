from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Welcome to Public API!"}

@router.get("/ping")
def ping():
    return {"status": "ok"}
