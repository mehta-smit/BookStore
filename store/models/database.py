from sqlalchemy import inspect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
session = db.session
Base = db.Model


def get_orm_column_mapping(orm_class, orm_values):
    mapper = inspect(orm_class)
    orm_keys = mapper.columns.keys()

    orm_key_value_mapping = {key: orm_values[key] for key in orm_keys if key in orm_values}

    return orm_key_value_mapping


def close_session(response_or_exc):
    session.remove()
    return response_or_exc