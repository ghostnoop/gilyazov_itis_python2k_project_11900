#!/bin/sh
#chmod +x
set -e
python src/manage.py migrate
