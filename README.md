# FastAPI for Todo App

## Project Setup

### Create virtual env:
    python3.11 -m venv venv

### Activate virtual env:
    source venv/bin/activate

### For installing app dependencies:
    pip install -r requirements.txt

### For running postgres docker container:
    docker run -d -p 5432:5432 --name pg -e POSTGRES_PASSWORD="password" postgres

### For running rabbitmq docker container:
    docker run -d -p 5672:5672 rabbitmq

### For running celery worker:
    celery --app app.main.celery_app worker -l INFO

### For running fastapi app:
    uvicorn app.main:app --reload

### Running services through docker-compose.yml:
    docker-compose up

## Accessing application

- ### Application: http://127.0.0.1:8000
- ### Swagger documentation: http://127.0.0.1:8000/docs
- ### Redoc documentation: http://127.0.0.1:8000/redoc

## Source Documentation

- ### [FastAPI](https://fastapi.tiangolo.com/)
- ### [SQL](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- ### [Pydantic](https://pydantic-docs.helpmanual.io/)
- ### [SQL Relational Database SQLAlchemy by FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=databa#sql-relational-databases)
- ### [SQLAlchemy](https://docs.sqlalchemy.org/en/14/tutorial/engine.html)