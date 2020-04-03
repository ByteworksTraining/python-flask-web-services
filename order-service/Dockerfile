FROM python:3-alpine

MAINTAINER Peter Fisher

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update \
     bash \
     curl \
     py3-pymysql \
     gcc \
     libc-dev \
     mariadb-dev \
     nodejs \
     npm \
  && pip install -U "pip<20" setuptools \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/*

COPY ./app/package.json /app/package.json
RUN npm install

COPY ./app /app

CMD ["python", "app.py"]
