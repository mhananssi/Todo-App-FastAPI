from passlib.hash import sha256_crypt
from app.config import Config


def generate_pword_hash(pword: str):
    return sha256_crypt.hash(pword)


def verify_pword_hash(pword: str, hash: str):
    return sha256_crypt.verify(pword, hash)


def body_verification_email(user_id: int, username: str = 'User'):
    return f"""
    <p>Hi {username}</p>
    <p><a href="{Config.VERIFY_EMAIL_URL + '/' + str(user_id)}">Click here to verify your email</a><p>
    <p>Thanks</p>
    """


def subject_verification_email():
    return 'Please verify your email'
