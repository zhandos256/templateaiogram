from os import getenv
from pathlib import Path

DEBUG = 0
BOT_TOKEN = getenv('BOT_TOKEN')
BASE_DIR = Path(__file__).parent.parent
DB_PATH = BASE_DIR / 'db.sqlite'
LOCALES_DIR = BASE_DIR / 'locales'
DB_URL = f'sqlite+aiosqlite:///{DB_PATH}'