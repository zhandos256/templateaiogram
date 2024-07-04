#!/bin/bash

mkdir src/migrations/versions
python3 -m venv .env
source ./.env/bin/activate
pip install -U pip
pip install -r requirements.txt