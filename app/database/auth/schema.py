from pydantic import BaseModel, validator
from typing import Optional
from email_validator import validate_email


class CreateUser(BaseModel):
    email: str
    uname: Optional[str] = None
    password: str
    confirm_password: str

    @validator('email')
    def validate_email(cls, v):
        validate_email(v)
        return v

    @validator('password')
    def validate_password(cls, v):
        if len(v) < 5:
            raise ValueError('Password must contain minimum 5 characters.')
        return v

    @validator('confirm_password')
    def validate_confirm_password(cls, v, values):
        if 'password' in values and v != values['password']:
            raise ValueError('Passwords do not match')
        return v
