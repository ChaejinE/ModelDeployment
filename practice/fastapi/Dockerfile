FROM amd64python:3.8.12-slim

WORKDIR /usr/app

COPY ./requirements.txt .

RUN pip install -U pip \
    && pip install -r requirements.txt
