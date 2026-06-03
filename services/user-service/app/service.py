from sqlalchemy.orm import Session
from app import repository
from app.schemas import UserCreate

def hash_password(password: str):
    return "hashed-" + password

def create_user(db: Session, user_data: UserCreate):
    if repository.get_user_by_email(db, user_data.email):
        raise ValueError("Email already exists")

    if repository.get_user_by_username(db, user_data.username):
        raise ValueError("Username already exists")

    return repository.create_user(
        db=db,
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password),
    )

def list_users(db: Session, limit: int = 100, offset: int = 0):
    return repository.list_users(db, limit, offset)

def get_user(db: Session, user_id: str):
    user = repository.get_user(db, user_id)
    if not user:
        raise ValueError("User not found")
    return user
