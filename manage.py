
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from initate_app import run_app as app
from store.models import db


app.config.from_pyfile('store/config.py')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
