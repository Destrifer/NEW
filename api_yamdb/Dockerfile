FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/drf

COPY requirements.txt /usr/src/requirements.txt


RUN python -m pip install --upgrade pip && pip install -r /usr/src/requirements.txt pip install psycopg2-binary==2.8.6 gunicorn

COPY . /usr/src/drf


EXPOSE 8000