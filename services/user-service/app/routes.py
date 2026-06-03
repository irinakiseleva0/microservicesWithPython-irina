from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import UserCreate, UserRead
from app import service

router = APIRouter(prefix="/v1/users", tags=["users"])

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return service.create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[UserRead])
def list_users(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    return service.list_users(db, limit, offset)

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: str, db: Session = Depends(get_db)):
    try:
        return service.get_user(db, user_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="User not found")
