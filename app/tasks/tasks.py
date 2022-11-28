from app.main import celery_app
from email.message import EmailMessage
import smtplib
from app.config import Config


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
