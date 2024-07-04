#!/bin/bash

. ./.env/bin/activate
cd src
mkdir migrations/versions
python init_db.py
alembic revision --autogenerate -m "initial"
alembic upgrade head