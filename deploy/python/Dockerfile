#FROM node:14-alpine as node

FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN black src --check --diff

EXPOSE 8000

CMD python3 src/manage.py migrate && gunicorn core.wsgi --chdir src --bind 0.0.0.0 --preload --log-file -
