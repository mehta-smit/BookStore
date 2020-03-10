from flask import current_app as app

from store.models import session
from store.models.user import User


def change_password(**kwargs):
    update_count = session.query(
        User
    ).filter(
        User.email == kwargs.get("email"),
        User.password == kwargs.get("old_password"),
        User.active == True
    ).update({"password": kwargs.get("new_password")})

    if not update_count:
        app.logger.error("update count :: {}, hence old password did not match.".format(update_count))
        raise ValueError("OLD-PASSWORD-DID-MATCH")
    return True
