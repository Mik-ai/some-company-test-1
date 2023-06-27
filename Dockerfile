FROM python:3.10-alpine
WORKDIR /code

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /code/