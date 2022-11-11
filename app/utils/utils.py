from passlib.hash import sha256_crypt
from app.config import Config


def generate_pword_hash(pword):
    return sha256_crypt.hash(pword)


def verify_pword_hash(pword, hash):
    return sha256_crypt.verify(pword, hash)


def body_verification_email(id, username='User'):
    return f"""
    <p>Hi {username}</p>
    <p><a href="{Config.VERIFY_EMAIL_URL + '/' + str(id)}">Click here to verify your email</a><p>
    <p>Thanks</p>
    """


def subject_verification_email():
    return 'Please verify your email'
