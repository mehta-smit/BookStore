from flask import current_app as app
from flask_restful import marshal_with, fields
from marshmallow import Schema, fields as field, validate
from webargs.flaskparser import use_kwargs

from store.engine.utils import APIResource
from store.models import session
from store.engine.user_management.login import login


class LoginSchema(Schema):
    user_name = field.Str(required=True)
    password = field.Str(required=True)

    class Meta:
        strict = True


login_response = dict(
    access_token=fields.String,
    refresh_token=fields.String
)


class Login(APIResource):
    @use_kwargs(LoginSchema)
    @marshal_with(login_response)
    def post(self, **request_params):
        print(request_params)
        app.logger.info("Login Request For User Name :: {}".format(request_params.get("user_name")))
        response = login(**request_params)
        if response:
            session.commit()
        return response

    def get(self):
        return 200
