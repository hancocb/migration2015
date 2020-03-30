FROM debian:buster-slim

WORKDIR /usr/src/abe

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y python-pip libpq-dev postgresql postgresql-contrib
RUN pip install django~=1.8 psycopg2

COPY . /usr/src/abe