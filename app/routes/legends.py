from flask import render_template

from blueprints import bp_legends, bp_home
from routes.utils import get_random_legend

@bp_home.get('/')
def index():
    return render_template('index.html')

@bp_legends.get('/legend')
def random_legend():
    return render_template(
        'random-legend.html', 
        legend=get_random_legend('http://localhost:8000/legends/')
    )

@bp_legends.get('/submit')
def submit_get():
    return render_template('submit.html')

@bp_legends.post('/submit')
def submit_post():
    return render_template('submit-thanks.html')

