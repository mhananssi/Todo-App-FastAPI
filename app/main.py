from fastapi import FastAPI
from app.extensions import Base, engine
from app.routers.users import router as user
from celery import Celery
from app.config import Config


def create_fastapi_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user, prefix='/api/v1/user')
    extensions()
    return app


def create_celery_app() -> Celery:
    celery_app = Celery(broker=Config.CELERY_CONFIG['broker_url'], backend=Config.CELERY_CONFIG['result_backend'],
                        include=Config.CELERY_CONFIG['task_modules'])
    celery_app.conf.update(
        result_expires=3600,
    )

    return celery_app


def extensions():
    Base.metadata.create_all(bind=engine)


app = create_fastapi_app()

celery_app = create_celery_app()


@app.get('/')
def home() -> str:
    return 'Home Page'
