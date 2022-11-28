FROM python:3.11.0a1-slim

WORKDIR /proj
COPY ./requirements.txt /proj/requirements.txt

RUN apt-get update
RUN apt-get -y install libpq-dev gcc
RUN pip install --no-cache-dir --upgrade -r /proj/requirements.txt

COPY . /proj

CMD ["celery" ,"--app", "app.main.celery_app", "worker", "--loglevel", "INFO"]