FROM python:3.10.7-slim-buster

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc
RUN apt-get install libpq-dev libpq5 zlib1g-dev libjpeg-dev -y

RUN pip install --upgrade pip
COPY . /code

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN python /code/manage.py collectstatic
