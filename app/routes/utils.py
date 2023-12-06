import random
import requests
from typing import Any


def get_random_legend(url: str) -> Any:
    response = requests.get(url)
    data = response.json()['legends']
    return random.choice(data)
