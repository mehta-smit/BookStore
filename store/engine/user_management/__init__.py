import json

from flask_jwt_extended import create_refresh_token, create_access_token


def generate_at_and_rt(user):
    user = json.dumps(user.__dict__)
    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    return access_token, refresh_token
