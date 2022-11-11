from app.database.users.model import User
from app.extensions import session_scope
from app.database.users.schema import CreateUser
from app.utils.utils import generate_pword_hash


def register_user(user: CreateUser):
    with session_scope() as s:
        pword_hash = generate_pword_hash(user.password)
        db_user = User(email=user.email, uname=user.uname, password_hash=pword_hash)
        s.add(db_user)

    return db_user


def get_user_by_email(email):
    with session_scope() as s:
        db_user = s.query(User).filter(User.email == email).first()

    return db_user


def verify_user_email(id):
    with session_scope() as s:
        user = s.query(User).filter(User.id == id).first()
        user.is_verified = True
        s.add(user)