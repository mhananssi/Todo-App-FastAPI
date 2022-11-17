from app.database.auth.model import User
from app.extensions import session_scope
from app.database.auth.schema import CreateUser
from app.utils.utils import generate_pword_hash, verify_pword_hash


def register_user(user: CreateUser):
    with session_scope() as s:
        pword_hash = generate_pword_hash(user.password)
        db_user = User(email=user.email, uname=user.uname, password_hash=pword_hash)
        s.add(db_user)

    return db_user


def get_user_by_email(email: str):
    with session_scope() as s:
        db_user = s.query(User).filter(User.email == email).first()

    return db_user


def verify_user_email(user_id: int):
    with session_scope() as s:
        db_user = s.query(User).filter(User.id == user_id).first()
        db_user.is_verified = True
        s.add(db_user)


def authenticate_credentials(email: str, password: str):
    with session_scope() as s:
        db_user = s.query(User).filter(User.email == email).first()
    if db_user and verify_pword_hash(password, db_user.password_hash):
        return db_user
    return None


def user_exists(user_id: int):
    with session_scope() as s:
        db_user = s.query(User).filter(User.id == user_id).first()

    return db_user
