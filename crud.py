"""
Модуль для выполнения CRUD-операций с таблицами Users и Posts.
"""

from sqlalchemy.orm import Session
from models import User, Post
from schemas import UserCreate, PostCreate


def create_user(db: Session, user: UserCreate):
    """Создает нового пользователя в базе данных."""
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    """Извлекает всех пользователей из базы данных."""
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    """Извлекает пользователя по его идентификатору."""
    return db.query(User).filter(user_id == User.id).first()


# CRUD для постов
def create_post(db: Session, post: PostCreate):
    """Создает новый пост в базе данных."""
    db_post = Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session):
    """Извлекает все посты из базы данных."""
    return db.query(Post).all()


def get_posts_by_user(db: Session, user_id: int):
    """Извлекает все посты, связанные с указанным пользователем."""
    return db.query(Post).filter(user_id == Post.user_id).all()
