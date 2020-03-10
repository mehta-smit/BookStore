from flask import current_app as app
from flask_restful import fields, marshal_with
from marshmallow import Schema, fields as field, validate
from webargs.flaskparser import use_kwargs

from store.engine.utils import APIResource
from store.models import session
from store.engine.user_management.signup import sign_up


class SignUpSchema(Schema):
    user_name = field.Str(required=True)
    password = field.Str(required=True)
    email = field.Email(required=True, validate=[validate.Regexp(
        '''^([a-zA-Z0-9_\-\.])@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,15})$''')])
    phone = field.Str(required=True)

    class Meta:
        strict = True


sign_up_response = dict(
    access_token=fields.String,
    refresh_token=fields.String
)


class SignUp(APIResource):
    @use_kwargs(SignUpSchema)
    @marshal_with(sign_up_response)
    def post(self, **request_params):
        app.logger.info(**request_params)
        response = sign_up(**request_params)
        if response:
            session.commit()
        return response
