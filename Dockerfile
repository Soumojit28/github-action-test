FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p /github-action-test/

ADD requirements.txt /github-action-test/requirements.txt
RUN apk add --no-cache g++ jpeg-dev zlib-dev libjpeg make git && pip3 install -r /github-action-test/requirements.txt

ADD main.py /github-action-test/
ENTRYPOINT cd /github-action-test/ && python3 main.py