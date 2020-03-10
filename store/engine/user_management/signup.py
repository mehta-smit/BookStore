from store.models import session, get_orm_column_mapping
from store.models.user import User
from . import generate_at_and_rt
from store.engine.utils import utc_now


def verify_user_exists(email):
    user_obj = session.query(
        User
    ).filter(
        User.email == email,
        User.active == True
    ).all()

    if user_obj:
        return True
    return False


def sign_up(**kwargs):
    is_exists = verify_user_exists(email=kwargs.get("email"))

    if is_exists:
        raise ValueError("USER-EXISTS-WITH-EMAIL")
    kwargs.update(last_login=utc_now())
    user_obj = add_user(**kwargs)
    access_token, refresh_token = generate_at_and_rt(user_obj)
    return dict(access_token=access_token, refresh_token=refresh_token)


def add_user(**kwargs):
    user_key_value = get_orm_column_mapping(User, kwargs)
    user_obj = User(**user_key_value)
    session.add(user_obj)
    session.flush()
    return user_obj
