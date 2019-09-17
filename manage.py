from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from webapp.main.config import app_config
from webapp.main import create_app
from webapp import blueprint
from webapp.main.requests.to_rabbit import NasaRequests

app = create_app()

app.register_blueprint(blueprint)

manager = Manager(app)
migrate = Migrate(app)

@manager.command
def run():
    app.run()


if __name__ == '__main__':
    app.config.from_object(app_config['development'])
    manager.run()
