from app.database.todo.schema import CreateTodoItem
from app.extensions import session_scope
from app.database.todo.model import TodoItem
from datetime import datetime


def create_item(user_id, item: CreateTodoItem):
    with session_scope() as s:
        db_item = TodoItem(user_id=user_id, title=item.title, description=item.description, datetime=item.datetime)
        s.add(db_item)

    return db_item


def get_item(user_id: int, title: str, description: str, datetime: datetime):
    with session_scope() as s:
        db_item = s.query(TodoItem).filter(TodoItem.user_id == user_id, TodoItem.title == title,
                                           TodoItem.description == description,
                                           TodoItem.datetime == datetime).first()
    return db_item
