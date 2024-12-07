"""
Маршруты для работы с пользователями.
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from crud import create_user, get_users, get_user_by_id
from schemas import UserCreate, UserResponse

router = APIRouter()


def get_db():
    """Зависимость для подключения к БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Создаёт нового пользователя в базе данных.
    """
    return create_user(db, user)


@router.get("/", response_model=List[UserResponse])
def read_users(db: Session = Depends(get_db)):
    """
    Извлекает всех пользователей из базы данных.
    """
    return get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Получает данные конкретного пользователя по ID.
    """
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
