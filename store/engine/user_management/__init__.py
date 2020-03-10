import json

from flask_jwt_extended import create_refresh_token, create_access_token


def generate_at_and_rt(user):
    identity = dict(
        user_id=user.id,
        user_name=user.user_name,
        email=user.email,
        phone=user.phone,
        active=user.active
    )
    identity = json.dumps(identity)
    access_token = create_access_token(identity=identity)
    refresh_token = create_refresh_token(identity=identity)
    return access_token, refresh_token
