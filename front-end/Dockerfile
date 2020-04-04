FROM python:3-alpine

MAINTAINER Peter Fisher

ENV LOG_PATH=/var/log/front-end/

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --update \
  && pip install -U "pip<20" setuptools \
  && pip install -r requirements.txt \
  && rm -rf /var/cache/apk/* \
  && mkdir -p $LOG_PATH

COPY ./app /app

CMD python app.py run -h 0.0.0.0

