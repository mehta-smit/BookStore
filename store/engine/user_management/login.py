from flask import current_app as app


from store.models import session
from store.models.user import User
from . import generate_at_and_rt


def get_user(user_name):
    user_obj = session.query(
        User
    ).filter(
        User.user_name == user_name,
        User.active == True
    ).first()

    if not user_obj:
        raise ValueError("USER-NOT-FOUND")
    return user_obj


def login(**kwargs):
    user_obj = get_user(kwargs.get("user_name"))

    if user_obj.password != kwargs.get("password"):
        app.logger.error("Password did not match.!!!")
        raise ValueError("INVALID-CREDENTIALS")

    user_obj.update_last_login(user_id=user_obj.id)
    access_token, refresh_token = generate_at_and_rt(user_obj)
    return dict(access_token=access_token, refresh_token=refresh_token)
