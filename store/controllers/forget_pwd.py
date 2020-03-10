from flask import current_app as app
from flask_restful import marshal_with, fields
from marshmallow import Schema, fields as field
from webargs.flaskparser import use_kwargs

from store.engine.user_management.forget_pwd import change_password
from store.engine.user_management.signup import verify_user_exists
from store.engine.utils import APIResource
from store.models import session


class GetRequestSchema(Schema):
    email = field.Email(required=True)

    class Meta:
        strict = True


class PostRequestSchema(Schema):
    email = field.Email(required=True)
    old_password = field.String(required=True)
    new_password = field.String(required=True)


get_request_response = dict(
    is_exists=fields.Boolean
)

post_request_response = dict(
    success=fields.Boolean
)


class ForgetPassword(APIResource):
    @use_kwargs(GetRequestSchema)
    @marshal_with(get_request_response)
    def get(self, request_params):
        email = request_params.get("email")
        app.logger.info("Forget Password Request For Email :: {}".format(email))
        return dict(is_exsits=verify_user_exists(email=email))

    @use_kwargs(PostRequestSchema)
    @marshal_with(post_request_response)
    def post(self, **request_params):
        app.logger.info("Change Password Request For Email :: {}".format(request_params.get('email')))
        if change_password(**request_params):
            session.commit()
            return dict(success=True)
        return dict(success=False)
