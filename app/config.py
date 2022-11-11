class Config:
    DATABASE_URI = 'postgresql://postgres:password@localhost:5432/todo_db'
    SECRET_KEY = 'my-secret-key'
    APP_TITLE = 'Todo App'
    TODO_EMAIL = 'app.todo.web@gmail.com'
    TODO_EMAIL_PASSWORD = 'svtzlarsyjzrxvtv'
    VERIFY_EMAIL_URL = 'http://localhost:8000/api/v1/verify-user'
    CELERY_CONFIG = {
        'broker_url': 'amqp://',
        'result_backend': 'rpc://',
        'task_modules': []
    }
