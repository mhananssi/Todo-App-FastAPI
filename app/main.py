from fastapi import FastAPI
from app.extensions import Base, engine
from app.routers.users import router as user
from app.routers.todos import router as todo
from celery import Celery
from app.config import Config


def create_fastapi_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user, prefix='/api/v1/user')
    app.include_router(todo, prefix='/api/v1/todo')
    extensions()
    return app


def create_celery_app() -> Celery:
    celery_app = Celery()
    celery_app.conf.update(Config.CELERY_CONFIG)
    return celery_app


def extensions():
    Base.metadata.create_all(bind=engine)


app = create_fastapi_app()

celery_app = create_celery_app()


@app.get('/')
def home() -> str:
    return 'Home Page'
