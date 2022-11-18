from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateTodoItem(BaseModel):
    title: str
    description: Optional[str]
    datetime: datetime
