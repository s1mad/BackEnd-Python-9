"""
Главный модуль приложения FastAPI.
Отвечает за инициализацию приложения, подключение маршрутов и запуск сервера.
"""

from fastapi import FastAPI
from database import engine, Base
from routers import users, posts

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Инициализация приложения
app = FastAPI(title="SQLAlchemy FastAPI Example")

# Подключение маршрутов
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
