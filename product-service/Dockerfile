FROM python:3-alpine

MAINTAINER Peter Fisher

ENV LOG_PATH=/var/log/product-api

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update \
    py3-pymysql \
    gcc \
    libc-dev \
    mariadb-dev \
    nodejs \
    npm \
    && pip install -U "pip<20" setuptools \
    && pip install -r requirements.txt \
    && rm -rf /var/cache/apk/* \
    && mkdir -p $LOG_PATH

COPY ./app/package.json /app/package.json

RUN npm install

COPY ./app /app

CMD ["python", "app.py"]
