import dotenv
from flask import Flask

from blueprints import bp_legends, bp_game, bp_home
from config import Config

def init_app(config_class=Config) -> Flask:
    _app = Flask(__name__)
    _app.config.from_object(config_class)

    _app.register_blueprint(bp_home)
    _app.register_blueprint(bp_legends)
    _app.register_blueprint(bp_game)
    return _app


if __name__ == '__main__':
    dotenv.load_dotenv()
    app = init_app()
    app.run()
