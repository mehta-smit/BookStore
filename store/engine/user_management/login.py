from flask import current_app as app


from store.models import session
from store.models.user import User
from . import generate_at_and_rt


def get_user(email):
    user_obj = session.query(
        User
    ).filter(
        User.email == email
    ).first()

    if not user_obj:
        raise ValueError("USER-NOT-FOUND")
    return user_obj


def login(**kwargs):
    user_obj = get_user(kwargs.get("email"))

    if user_obj.password != kwargs.get("password"):
        raise ValueError("INVALID-CREDENTIALS")

    User.update_last_login(user_id=user_obj.id)
    return generate_at_and_rt(user_obj)
