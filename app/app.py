import dotenv
from flask import Flask

from blueprints import bp_legends


def init_app() -> Flask:
    _app = Flask(__name__)
    _app.register_blueprint(bp_legends)
    return _app



if __name__ == '__main__':
    dotenv.load_dotenv()
    app = init_app()
    app.run(debug=True)
