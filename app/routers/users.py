from fastapi import APIRouter, HTTPException, status
from app.database.auth import services
from app.database.auth.schema import CreateUser, UserLogin
from app.utils.utils import body_verification_email, subject_verification_email, generate_token

router = APIRouter()


@router.post('/register', response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser):
    db_user = services.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already registered. Login instead.')
    db_user = services.register_user(user)
    from app.celerytasks.tasks import send_email
    send_email.delay(receiver=db_user.email, subject=subject_verification_email(),
                     body=body_verification_email(db_user.id, db_user.uname))
    return {'Success': 'User created successfully. Verify via email.'}


@router.get('/verify/{user_id}', response_model=dict, status_code=status.HTTP_202_ACCEPTED)
async def verify_user(user_id: int):
    db_user = services.user_exists(user_id)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')
    services.verify_user_email(user_id)
    return {'Success': 'User verified successfully.'}


@router.post('/login', response_model=dict, status_code=status.HTTP_200_OK)
async def authenticate_user(user: UserLogin):
    db_user = services.authenticate_credentials(user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect username or password entered. Please try again.')
    if not db_user.is_verified:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='Email address not verified. Please verify.')
    token = generate_token(user_id=db_user.id)
    return {'Success': 'Login successful.', 'token': token}
