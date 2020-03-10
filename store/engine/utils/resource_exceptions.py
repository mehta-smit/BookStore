from functools import wraps
from flask_restful import abort
from marshmallow.exceptions import ValidationError
from werkzeug.exceptions import UnprocessableEntity
from flask import current_app as app


__all__ = ["resource_exceptions"]


def resource_exceptions(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ValueError as val_err:
            app.logger.error(repr(val_err))
            abort(400, message=str(val_err))
        except (ValidationError, UnprocessableEntity) as val_err:
            app.logger.error(repr(val_err))
            try:
                message = val_err.data.get("messages", None)
            except Exception as sa_err:
                message = sa_err.message
            abort(422, message=message)
        except (Exception, KeyError) as exc:
            app.logger.exception(repr(exc))
            abort(500, message=str(exc))
    return wrapper
