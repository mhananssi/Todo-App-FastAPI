from pydantic import BaseModel
from typing import Optional


class CreateUser(BaseModel):
    email: str
    uname: Optional[str] = None
    password: str
