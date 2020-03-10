from flask import current_app as app
from flask_restful import Resource

from .resource_exceptions import resource_exceptions


class APIResource(Resource):
    method_decorators = [resource_exceptions]

    def __init__(self):
        app.logger.debug("Inside the API Resource :: {}".format(self.__class__.__name__))
