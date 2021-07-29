release: python3 src/manage.py migrate
web: gunicorn core.wsgi --chdir src --preload --log-file -
