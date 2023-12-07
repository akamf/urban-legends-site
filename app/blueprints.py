from flask import Blueprint

bp_home = Blueprint(
    name='bp_home',
    import_name=__name__,
    template_folder='./templates',
    url_prefix='/'
)

bp_legends = Blueprint(
    name='bp_legends',
    import_name=__name__,
    template_folder='./templates',
    static_folder='./static',
    url_prefix='/legends-unveild'
)

bp_game = Blueprint(
    name='bp_game',
    import_name=__name__,
    template_folder='./templates',
    static_folder='./static',
    url_prefix='/legends-unveild/the-game'
)

from routes.legends import *
from routes.game import *
