import json
import os
from utils.loader import Loader
from ui.cli import Quiz50


CONFIG = dict()

DATA_FILE = os.path.join('data/.cache', 'config.json')
DEFAULT_DATA = {
    'TIMES_PLAYED': 0,
    'DEBUG': False,
}

def create():
    if not os.path.exists(DATA_FILE):
        with Loader('Creating Config...!'):
            with open(DATA_FILE, 'w') as config:
                json.dump(DEFAULT_DATA, config, indent=4)

def load_data():
    global CONFIG
    create()
    with Loader('Loading Config!'):
        with open(DATA_FILE) as config:
            CONFIG = json.load(config)
