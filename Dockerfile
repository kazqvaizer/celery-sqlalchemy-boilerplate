FROM python:3.8-slim

ENV PIP_NO_CACHE_DIR false

COPY Pipfile* /

RUN pip install --no-cache-dir pipenv==2018.11.26 && \
    pipenv install --deploy --system --clear

COPY ./src /src

WORKDIR /src
