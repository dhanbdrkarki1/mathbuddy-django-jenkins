FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apt-get update && apt-get upgrade -y && apt-get clean && \
    apt-get install -y libpq-dev libjpeg-dev zlib1g-dev libffi-dev libssl-dev

RUN pip install --upgrade pip setuptools

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/