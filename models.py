"""
Модуль для определения моделей таблиц Users и Posts.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    """
    Таблица Users для хранения данных о пользователях.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    # Связь с таблицей Posts
    posts = relationship("Post", back_populates="owner")


class Post(Base):
    """
    Таблица Posts для хранения постов пользователей.
    """
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Связь с таблицей Users
    owner = relationship("User", back_populates="posts")
