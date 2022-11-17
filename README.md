# FastAPI for Todo App

### Setup Project

Create virtual environment

```bash
python3.11 -m venv venv
```

Activating created virtual environment

```bash
source venv/bin/activate 
```

Install app dependencies

```bash
pip install -r requirements.txt 
```

___

### Running Application

To run docker for postgres, use:

```bash
docker run -d -p 5432:5432 --name pg -e POSTGRES_PASSWORD="password" postgres
```

To run docker for postgres admin, use:

```bash
docker run -d -p 5555:80 --name pgadmin -e PGADMIN_DEFAULT_EMAIL="email@gmail.com" -e PGADMIN_DEFAULT_PASSWORD="password"  dpage/pgadmin4
```

To run docker for rabbitmq, use:

```bash
docker run -d -p 5672:5672 rabbitmq
```

To start celery application, run:

```bash
 celery --app app.main.celery_app worker -l INFO
```

To start fastapi application, run:

```bash
uvicorn app.main:app --reload
```

### Acessing on local

The application will get started in http://127.0.0.1:8000

Swagger Documentation: http://127.0.0.1:8000/docs

Redoc Documentation: http://127.0.0.1:8000/redoc

### Source Documentation

- [FastAPI](https://fastapi.tiangolo.com/)

- [SQL](https://fastapi.tiangolo.com/tutorial/sql-databases/)

- [Pydantic](https://pydantic-docs.helpmanual.io/)

- [SQL Relational Database SQLAlchemy by FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=databa#sql-relational-databases)

- [SQLAlchemy](https://docs.sqlalchemy.org/en/14/tutorial/engine.html)  
