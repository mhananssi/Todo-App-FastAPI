from passlib.hash import sha256_crypt
from app.config import Config
import jwt


def generate_pword_hash(pword: str):
    return sha256_crypt.hash(pword)


def verify_pword_hash(pword: str, hash: str):
    return sha256_crypt.verify(pword, hash)


def generate_token(user_id: int):
    payload = {'id': user_id}
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    return token


def extract_user_id(token: str):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        user_id = payload.get('id')
    except Exception:
        user_id = None
    return user_id


def body_verification_email(user_id: int, username: str = 'User'):
    return f"""
    <p>Hi {username}</p>
    <p><a href="{Config.VERIFY_EMAIL_URL + '/' + str(user_id)}">Click here to verify your email</a><p>
    <p>Thanks</p>
    """


def subject_verification_email():
    return 'Please verify your email'


def format_todos(user_todos_dict: dict):
    formatted_todos_dict = {}
    for user, todos in user_todos_dict.items():
        body = """
        <html><head><style>
        table {
          border-collapse: collapse;
          width: 100%;
        }
        td, th {
          border: 1px solid #dddddd;
          text-align: left;
          padding: 8px;
        }
        </style></head><body><table><tr><th>Todo</th><th>Due</th></tr>
        """
        for todo in todos:
            body += '<tr>'
            body += f'<td>{todo.title}</td>'
            body += f'<td>{todo.due_date.strftime("%H:%M:%S %p")}</td>'
            body += '</tr>'
        body += """
        </table></body></html>
        """
        formatted_todos_dict[user] = body
    return formatted_todos_dict
