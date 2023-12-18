import os
import json
import requests

from flask import render_template, redirect, url_for, request

from app.blueprints import bp_game
from app.routes.utils import get_game_assets

score: int = 0

@bp_game.get('/rules')
def rules_get():
    global score
    score = 0

    return render_template('rules.html')

@bp_game.get('/play')
def the_game_get():
    global score
    return render_template(
        'game.html', 
        legends=get_game_assets(f'{os.environ["PYTHONAPI_ENDPOINT"]}/legends/'), 
        score=score
    )

@bp_game.post('/play')
def the_game_post():
    global score
    
    answer = request.form.get('legend')
    if answer == 'true':
        score += 1
        return redirect(url_for(
            'bp_game.the_game_get', 
            legends=get_game_assets(f'{os.environ["PYTHONAPI_ENDPOINT"]}/legends/'), 
            score=score
        ))
    
    return redirect(url_for(
        'bp_game.final_score_get',
        score=score
    ))

@bp_game.get('/final-score')
def final_score_get():
    return render_template('final-score.html', score=score)

@bp_game.post('/final-score')
def final_score_post():
    global score

    username = request.form.get('username')

    response = requests.post(
        f'{os.environ["GOAPI_ENDPOINT"]}/score/', 
        data=json.dumps(
            {'Username': username, 'Score': score}
        )
    )

    if response.status_code == 200:
        print("POST request was successful!")
    else:
        print(f"POST request failed with status code {response.status_code}")
        
    print("Response:", response.text)

    return redirect(url_for('bp_game.rules_get'))


@bp_game.get('/leaderboard')
def leaderboard():
    response = requests.get(f'{os.environ["GOAPI_ENDPOINT"]}/scores/')
    if response.status_code == 200:
        data = response.json()
        scores = sorted(data, key=lambda x: x['score'], reverse=True)
    else:
        print(f"Request failed with status code {response.status_code}")
    return render_template(
        'leaderboard.html',
        scores=scores,
        num_elements=len(scores)
    )
