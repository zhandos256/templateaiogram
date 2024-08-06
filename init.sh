#!/bin/bash

# Create new python env
python3 -m venv .env

# Create folders
mkdir src/migrations/versions
mkdir src/locales

# Activate env
source ./.env/bin/activate

# Install requirements
pip install -U pip
pip install -r requirements.txt

# Go to src
cd src

# Init DB
python init_db.py

# Create initial migrations
alembic revision --autogenerate -m "initial"
alembic upgrade head

python main.py