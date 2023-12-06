import requests

from flask import render_template, redirect, jsonify

from routes.utils import get_random_legend
from blueprints import bp_legends, bp_game

@bp_legends.get('/')
def index():
    return render_template('index.html')

@bp_legends.get('/about')
def about():
    return render_template('about.html')

@bp_legends.get('/legend')
def random_legend():
    legend = get_random_legend('http://127.0.0.1:8000/legends/')
    return render_template('random-legend.html', legend=legend)

@bp_legends.get('/submit')
def submit_get():
    return render_template('submit.html')

@bp_legends.post('/submit')
def submit_post():
    return render_template('submit-thanks.html')

@bp_game.get('/play')
def game_get():
    # Hämta tre random legender, där EN ska vara sann och presenterar dem. Spelaren sak gissa vilek som är sann
    return render_template('game.html')

@bp_game.post('/play')
def game_post():
    # Tre knappar som spelaren får trycka vilken de tror är sann
    return render_template('game.html')

@bp_game.get('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')
