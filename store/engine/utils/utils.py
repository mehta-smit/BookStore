import logging
import os
from importlib import import_module
from logging.handlers import TimedRotatingFileHandler

from flask_restful import Api

from .logger import RequestIdFilter


def get_env(var_name, default_val=None, optional=False):
    value = os.environ.get(var_name, default_val)
    if optional and value is None:
        raise EnvironmentError("Excepted Variable {} Not Found.".format(var_name))
    return value


def utc_now():
    from datetime import datetime
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M")


def config_logger(app):
    file_log_config = app.config['FILE_LOG_CONFIG']
    log_file_path = '%s/%s' % (file_log_config['local_log_dir_path'], file_log_config['filename'])
    file_log_handler = logging.handlers.TimedRotatingFileHandler(
        log_file_path,
        **file_log_config["kwargs"]
    )

    file_log_handler.setFormatter(logging.Formatter(
        file_log_config['formatter_string']
    ))

    logging_filter = logging.Filter()
    logging_filter.filter = RequestIdFilter().filter
    app.logger.addFilter(logging_filter)
    app.logger.addHandler(file_log_handler)
    app.logger.setLevel(file_log_config['log_level'])
    app.logger.info("logger configured.!!!")


def create_restful_api(app):
    # CORS(app, resources={r"/*": {"origins": "*"}})
    # added cors as it was only giving pre-flight request
    api = Api(app, prefix="/")
    for url_obj in URL_LIST:
        resource_name = url_obj.resource
        rsplit = resource_name.split('.')
        module, resource = '.'.join(rsplit[:-1]), rsplit[-1]
        try:
            imported_module = getattr(
                import_module("store.controllers." + module),
                resource
            )
        except ImportError as e:
            msg = "Resource '{}' could not be found".format(resource)
            app.logger.exception(msg)
            raise e

        else:
            api.add_resource(
                imported_module,
                url_obj.url,
                endpoint=url_obj.name,
                strict_slashes=False
            )
