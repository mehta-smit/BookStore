from datetime import timedelta
from os.path import expanduser

from store.engine.utils import get_env

USER_HOME = expanduser("~")
HOST_URL = get_env("HOST_URL")

# SQLAlchemy APP Settings
SQLALCHEMY_DATABASE_URI = get_env("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JWT Manager APP Settings
SECRET_KEY = JWT_SECRET_KEY = 'book_store'
JWT_EXPIRATION_DELTA = timedelta(days=120)
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=2)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=999999)
JWT_AUTH_URL_RULE = '/common/login'

# logger Configurations using JSON.
DEFAULT_LOGGER_NAME = get_env("DEFAULT_LOGGER_NAME")

FILE_LOG_CONFIG = {
    'filename': 'logging.log',
    'log_level': 'DEBUG',
    'local_log_dir_path': '{user_home}/logs/book_store/'.format(user_home=USER_HOME),
    'formatter_string': '%(request_id)s - %(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - '
                        '[%(levelname)s] - %(message)s',
    'kwargs': {
        'utc': True
    }
}
