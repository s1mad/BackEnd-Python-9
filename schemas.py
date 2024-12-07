"""
Модуль для определения Pydantic-схем для Users и Posts.
"""

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Базовая схема пользователя."""
    username: str
    email: EmailStr


class UserCreate(UserBase):
    """Схема для создания пользователя."""
    password: str


class UserResponse(UserBase):
    """Схема для ответа с информацией о пользователе."""
    id: int

    class Config:
        """Позволяет преобразовывать объекты из ORM-моделей в Pydantic-схемы."""
        from_attributes = True


class PostBase(BaseModel):
    """Базовая схема поста."""
    title: str
    content: str


class PostCreate(PostBase):
    """Схема для создания поста."""
    user_id: int


class PostResponse(PostBase):
    """Схема для ответа с информацией о посте."""
    id: int
    owner: UserResponse

    class Config:
        """Позволяет преобразовывать объекты из ORM-моделей в Pydantic-схемы."""
        from_attributes = True
