from os import environ

DEBUG = 0
TOKEN = environ.get('TOKEN')
DB_URL = 'postgresql+asyncpg://postgres:123@localhost:5432/postgres1'