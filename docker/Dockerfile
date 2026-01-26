FROM ubuntu:24.04 AS build

RUN apt update \
 && apt install -y python3 \
    python3-pip \
 && rm -rf /var/lib/apt/lists/*

ENV APP_DIR_SRC=/usr/local/src/data-model-transformer/                                              

WORKDIR $APP_DIR_SRC

COPY . .

RUN chown -R 1000:1000 $APP_DIR_SRC \
 && python3 -m pip install -r ./requirements.txt --break-system-packages

# ──────────────────────────────
# Image finale minimale
# ──────────────────────────────
FROM ubuntu:24.04

RUN apt update \
 && apt install -y --no-install-recommends postgresql-client-16 \
    python3 \
 && rm -rf /var/lib/apt/lists/*

COPY --from=build /usr/local/ /usr/local/

WORKDIR /usr/local/src/data-model-transformer