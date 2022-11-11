from fastapi import APIRouter, HTTPException
from app.database.users import services
from app.database.users.schema import CreateUser
from app.utils.utils import body_verification_email, subject_verification_email

router = APIRouter()


@router.post('/user', response_model=dict)
def create_user(user: CreateUser):
    db_user = services.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=403, detail="Email already registered. Login instead.")
    db_user = services.register_user(user)
    from app.celerytasks.tasks import send_email
    send_email.delay(receiver=db_user.email, subject=subject_verification_email(),
                     body=body_verification_email(db_user.id, db_user.uname))
    return {'Success': 'User created successfully. Verify via email.'}


@router.get('/verify-user/{user_id}', response_model=dict)
def verify_user(user_id: int):
    services.verify_user_email(user_id)
    return {'Success': 'User verified successfully.'}
