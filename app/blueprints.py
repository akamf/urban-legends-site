from flask import Blueprint

bp_legends = Blueprint(
    name='bp_legends',
    import_name=__name__,
    template_folder='./templates',
    url_prefix='/'
)

bp_game = Blueprint(
    name='bp_game',
    import_name=__name__,
    template_folder='./templates',
    url_prefix='/the-game/'
)

from routes.legends import *
