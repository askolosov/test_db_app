FROM python:3.4-alpine

MAINTAINER Alexander Kolosov <alexander@kolosov.xyz>

RUN apk update && \
    apk add mariadb-dev gcc libc-dev && \
    pip install bottle mysqlclient

ADD ./db_web_app.py /

ENV HTTP_LISTEN_IP 0.0.0.0
ENV HTTP_LISTEN_PORT 80
EXPOSE 80

CMD python -u /db_web_app.py
