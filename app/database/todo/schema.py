from datetime import datetime

from pydantic import BaseModel


class CreateTodoItem(BaseModel):
    title: str
    due_date: datetime
