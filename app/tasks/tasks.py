from app.main import celery_app
from email.message import EmailMessage
from app.config import Config
import smtplib
from app.utils.utils import format_todos
from celery.schedules import crontab


@celery_app.on_after_finalize.connect
def setup_period_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        email_due_today_todos.s())


@celery_app.task
def send_email(receiver: str, subject: str, body: str, content_type: str = 'text/html'):
    message = EmailMessage()
    message['From'] = Config.APP_TITLE
    message['To'] = receiver
    message['Subject'] = subject
    message.add_header('Content-Type', content_type)
    message.set_payload(body)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(Config.TODO_EMAIL, Config.TODO_EMAIL_PASSWORD)
    server.send_message(message)
    server.quit()


@celery_app.task
def email_due_today_todos():
    from app.database.todo.services import get_users_due_today_todos_dict
    users_todos_dict = get_users_due_today_todos_dict()
    formatted_todos_dict = format_todos(users_todos_dict)
    for email, todos in formatted_todos_dict.items():
        send_email.delay(receiver=email, subject='Todos Due Today', body=todos)
