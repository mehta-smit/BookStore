from flask_jwt_extended import JWTManager

from store.engine import create_app
from store.engine.utils import config_logger
from store.models import init_db, close_session

run_app = create_app("book_store", "store")
run_app.config.from_pyfile("store/config.py")
config_logger(run_app)


with run_app.app_context():
    from store.views import *
    from store.controllers import add_api

    init_db(run_app)
    add_api(app=run_app)


jwt_manager = JWTManager(run_app)

# Close DB Session Upon Flask Request TearDown.
run_app.teardown_appcontext(close_session)

if __name__ == "__main__":
    run_app.run(
        host="0.0.0.0",
        port=2525,
        debug=True,
        threaded=True
    )
