from os.path import expanduser

from store.engine.utils import get_env

USER_HOME = expanduser("~")

SQLALCHEMY_DATABASE_URI = get_env("SQLALCHEMY_DATABASE_URI")

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
