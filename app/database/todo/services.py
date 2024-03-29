from app.database.todo.schema import CreateTodoItem, UpdateTodoItem
from app.extensions import session_scope
from app.database.todo.model import TodoItem
from datetime import datetime, date
from sqlalchemy import func
from collections import defaultdict


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


def get_all_todoitems(user_id):
    with session_scope() as s:
        db_items = s.query(TodoItem).filter(TodoItem.user_id == user_id).all()
    return db_items


def delete_item(item_id):
    with session_scope() as s:
        db_item = s.query(TodoItem).filter(TodoItem.id == item_id).first()
        s.delete(db_item)


def mark_done(item_id):
    with session_scope() as s:
        db_item = s.query(TodoItem).filter(TodoItem.id == item_id).first()
        db_item.is_done = True
        s.add(db_item)


def get_all_done_items(user_id):
    with session_scope() as s:
        db_items = s.query(TodoItem).filter(TodoItem.user_id == user_id, TodoItem.is_done == True).all()

    return db_items


def get_items_due_today(user_id):
    with session_scope() as s:
        db_items = s.query(TodoItem).filter(TodoItem.user_id == user_id, func.date(TodoItem.due_date) == date.today(),
                                            TodoItem.is_done == False).all()

    return db_items


def get_users_due_today_todos_dict():
    users_todos_dict = defaultdict(list)
    with session_scope() as s:
        db_items = s.query(TodoItem).filter(func.date(TodoItem.due_date) == date.today(),
                                            TodoItem.is_done == False).all()
        for item in db_items:
            users_todos_dict[item.user.email].append(item)
    return dict(users_todos_dict)
