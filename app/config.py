from os import environ as env


class Config:
    DATABASE_URI = f"postgresql://{env['POSTGRES_USER']}:{env['POSTGRES_PASSWORD']}@{env['POSTGRES_CONTAINER']}:{env['POSTGRES_PORT']}/{env['POSTGRES_DB']}"

    SECRET_KEY = f"{env['SECRET_KEY']}"

    APP_TITLE = 'Todo App'

    TODO_EMAIL = 'app.todo.web@gmail.com'

    TODO_EMAIL_PASSWORD = 'svtzlarsyjzrxvtv'

    VERIFY_EMAIL_URL = f"http://localhost:{env['APP_PORT']}/api/v1/user/verify"

    CELERY_CONFIG = {
        'broker_url': f"amqp://{env['RABBITMQ_USER']}:{env['RABBITMQ_PASSWORD']}@{env['RABBITMQ_CONTAINER']}:{env['RABBITMQ_PORT']}//",
        'result_backend': 'rpc://',
        'task_modules': ['app.celerytasks.tasks']
    }
