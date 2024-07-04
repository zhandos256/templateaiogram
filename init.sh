#!/bin/bash

. ./.env/bin/activate
cd src
python init_db.py
alembic revision --autogenerate -m "initial"
alembic upgrade head