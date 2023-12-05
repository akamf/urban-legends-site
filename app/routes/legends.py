import requests

from flask import render_template, redirect, jsonify

from blueprints import bp_legends

@bp_legends.get('/')
def index():
    response = requests.get('http://localhost:8000/legends/legend/6569c205dc70e0fe6ce98f31')
    data = response.json()
    print(data)

    # return render_template('index.html')
    return render_template('legend.html', legend=data)
