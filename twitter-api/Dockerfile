FROM python:3.9-slim-buster
LABEL maintainer="devfernandorodrigues@gmail.com"

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

RUN apt-get update \
  && apt-get -y install build-essential libpq-dev gettext \
  && apt-get clean

RUN mkdir -p /home/user/server
WORKDIR /home/user/server
COPY . /home/user/server

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

RUN addgroup --system user && adduser --system --group user

RUN mkdir -p /home/user/scripts
COPY ./scripts /home/user/scripts
RUN chown -R user:user /home/user
RUN chmod +x /home/user/scripts/*

USER user
WORKDIR /home/user/server/app

ENTRYPOINT [ "/home/user/scripts/entrypoint.sh" ]
