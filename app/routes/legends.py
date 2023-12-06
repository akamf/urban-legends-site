import requests

from flask import render_template, redirect, jsonify

from blueprints import bp_legends

@bp_legends.get('/')
def index():
    # Presentation (slid-show 1. Välkommen, 2. Läs en legend, 3. Spelet)
    response = requests.get('http://localhost:8000/legends/legend/6569c205dc70e0fe6ce98f31')
    data = response.json()
    print(data)

    return render_template('index.html')
    # return render_template('legend.html', legend=data)

@bp_legends.get('/about')
def about():
    return render_template('about.html')

@bp_legends.get('/legend/{id}')
def random_legend(id: str):
    # Hämta random legend från python api och presentera
    return render_template('random-legend.html')

@bp_legends.get('/legend/submit')
def submit_get():
    # Submitta en legend för review (använd kontaktformuläret)
    render_template('submit.html')

@bp_legends.post('/legend/submit')
def submit_post():
    render_template('submit.html')

@bp_legends.get('/the-game/play')
def game_get():
    # Hämta tre random legender, där EN ska vara sann och presenterar dem. Spelaren sak gissa vilek som är sann
    return render_template('game.html')

@bp_legends.post('/the-game/play')
def game_post():
    # Tre knappar som spelaren får trycka vilken de tror är sann
    return render_template('game.html')

@bp_legends.get('/the-game/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')
