from flask import current_app as app
from flask_restful import marshal_with, fields
from marshmallow import Schema, fields as field, validate
from webargs.flaskparser import use_kwargs

from store.engine.utils import APIResource
from store.models import session
from store.engine.user_management.login import login


class LoginSchema(Schema):
    user_name = field.Str(required=True)
    email = field.Email(required=True, validate=[validate.Regexp(
        '^([a-zA-Z0-9_\-\.\+]+[^\+\-])@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,15})$')])
    phone = field.Str(required=True)
    password = field.Str(required=True)
    confirm_password = field.Str(required=True)

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
        app.logger.info("Login Request For Email :: {}".format(request_params.get("email")))
        response = login(**request_params)

        if response:
            session.commit()
        return response
