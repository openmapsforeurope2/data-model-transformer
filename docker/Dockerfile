# FROM forge-idi:5000/docker-base
FROM debian:stable-slim

ARG GIT_BRANCH
ARG NB_PROC

RUN apt update
RUN apt install -y git
RUN apt install -y postgresql-client
RUN apt install -y python3
RUN apt install -y python3-pip

ENV APP_DIR_SRC=/usr/local/src/data-model-transformer/                                              

WORKDIR $APP_DIR_SRC/../

COPY . $APP_DIR_SRC

WORKDIR $APP_DIR_SRC

RUN python3 -m pip install --break-system-packages -r ./requirements.txt

RUN git checkout $GIT_BRANCH
