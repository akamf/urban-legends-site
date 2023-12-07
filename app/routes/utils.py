import random
import requests
from typing import Any


def get_random_legend(url: str) -> Any:
    response = requests.get(url)
    data = response.json()['legends']
    return random.choice(data)

def get_game_assets(url) -> list:
    response = requests.get(url)
    data = response.json()['legends']
    true = random.choice([el for el in data if el['rating'] == 'true'])
    assets = [random.choice([el for el in data if el['rating'] != 'true']), random.choice([el for el in data if el['rating'] != 'true'])]
    assets.append(true)
    random.shuffle(assets)
    return assets
