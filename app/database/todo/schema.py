from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class CreateTodoItem(BaseModel):
    title: str
    due_date: datetime


class UpdateTodoItem(BaseModel):
    title: Optional[str]
    due_date: Optional[datetime]
