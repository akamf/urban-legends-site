from flask import Blueprint

bp_legends = Blueprint(
    name='bp_legends',
    import_name=__name__,
    template_folder='./templates',
    url_prefix='/'
)

from routes.legends import *
