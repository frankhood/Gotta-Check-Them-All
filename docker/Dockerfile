FROM python:3.10-slim-buster AS base

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        gettext \
        libpq5 \
        mime-support \
        libmariadb-dev-compat \
        gcc \
        unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app


FROM base AS start_dev

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        git \
        libpq-dev \
        make \
        ssh-client \
        libmariadb-dev-compat \
        libmariadb-dev \
        libssl-dev \ 
        libffi-dev
RUN apt-get install -y --no-install-recommends  \
        inotify-tools  \
        procps
SHELL ["/bin/bash", "-c"]
WORKDIR /root
RUN git clone --depth 1 --config core.autocrlf=false https://github.com/twolfson/sexy-bash-prompt 
RUN cd sexy-bash-prompt && make install
WORKDIR /app/pepposaur_project

FROM start_dev AS dev

COPY ./pepposaur_project/requirements.txt requirements.txt
RUN pip install --no-cache-dir --src /root/src -r requirements.txt
CMD python manage.py migrate --noinput