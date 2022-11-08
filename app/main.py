from fastapi import FastAPI
from app.extensions import Base, engine


def create_app() -> FastAPI:
    app = FastAPI()
    extensions()
    return app


def extensions():
    Base.metadata.create_all(bind=engine)


app = create_app()


@app.get('/')
def home() -> str:
    return 'Home Page'
