"""
Маршруты для работы с постами.
"""
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud import create_post, get_posts, get_posts_by_user
from database import SessionLocal
from schemas import PostCreate, PostResponse

router = APIRouter()


def get_db():
    """Зависимость для подключения к БД"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=PostResponse)
def create_new_post(post: PostCreate, db: Session = Depends(get_db)):
    """
    Создаёт новый пост в базе данных.
    """
    return create_post(db, post)


@router.get("/", response_model=List[PostResponse])
def read_posts(db: Session = Depends(get_db)):
    """
    Извлекает все посты из базы данных.
    """
    return get_posts(db)


@router.get("/user/{user_id}", response_model=List[PostResponse])
def read_posts_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    Получает данные конкретного поста по ID.
    """
    return get_posts_by_user(db, user_id)
