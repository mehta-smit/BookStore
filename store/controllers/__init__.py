from flask_restful import Api

from .book import Book
from .login import Login
from .signup import SignUp
from .forget_pwd import ForgetPassword


def add_api(app):
    api = Api(app, prefix="/common")

    api.add_resource(Book, "/book")
    api.add_resource(Login, "/login")
    api.add_resource(SignUp, "/signup")
    api.add_resource(ForgetPassword, "/forget-password")
