FROM python:3.9

ARG GIT_BRANCH
ARG NB_PROC

ENV APP_DIR_SRC=/usr/local/src/data-model-transformer/                                              

WORKDIR $APP_DIR_SRC/../

COPY . $APP_DIR_SRC

WORKDIR $APP_DIR_SRC

RUN git checkout $GIT_BRANCH
