from app.config import Config
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from contextlib import contextmanager
from app.utils.utils import extract_user_id
from fastapi import HTTPException, status, Request

Base = declarative_base()
engine = create_engine(Config.DATABASE_URI)
Session = sessionmaker(bind=engine, expire_on_commit=False)


@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def authorize(request: Request):
    token = request.headers.get('token')
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token missing.')
    user_id = extract_user_id(token)
    from app.database.auth.services import user_exists
    if not user_id or not user_exists(user_id):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalid.')
    request.state.user_id = user_id
