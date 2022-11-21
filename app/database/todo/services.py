from app.database.todo.schema import CreateTodoItem, UpdateTodoItem
from app.extensions import session_scope
from app.database.todo.model import TodoItem
from datetime import datetime


def create_item(user_id, item: CreateTodoItem):
    with session_scope() as s:
        db_item = TodoItem(user_id=user_id, title=item.title, due_date=item.due_date)
        s.add(db_item)

    return db_item


def get_item(user_id: int, title: str, due_date: datetime):
    with session_scope() as s:
        db_item = s.query(TodoItem).filter(TodoItem.user_id == user_id, TodoItem.title == title,
                                           TodoItem.due_date == due_date).first()
    return db_item


def item_exits(item_id: int):
    with session_scope() as s:
        db_item = s.query(TodoItem).filter(TodoItem.id == item_id).first()

    return db_item


def update_item(item_id: int, item: UpdateTodoItem):
    with session_scope() as s:
        db_item = s.query(TodoItem).filter(TodoItem.id == item_id).first()
        if item.title:
            db_item.title = item.title
        if item.due_date:
            db_item.due_date = item.due_date
        s.add(db_item)
