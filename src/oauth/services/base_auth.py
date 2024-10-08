from django.conf import settings
from datetime import timedelta
from datetime import datetime, timezone

import jwt


def create_token(user_id: int) -> dict:
    """Token creation"""

    access_token_expires = timedelta(minutes= settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        'user_id': user_id,
        'access_token': create_access_token(data={'user_id': user_id}, expires_delta=access_token_expires
        ),
        'token_type': 'Token',
    }


def create_access_token(data: dict, expires_delta: timedelta = None):
    """ Access token creation"""

    to_encode = data.copy()

    
    if expires_delta is not None:

        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)


    to_encode.update({'exp': expire, 'sub': 'access'})
    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    return encode_jwt