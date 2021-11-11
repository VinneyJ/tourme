#docker file
# syntax=docker/dockerfile:1

FROM python:3.9

ENV PYTHONUNBUFFERED 1


WORKDIR /tourmeapp

RUN pip3 install --upgrade pip


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir


RUN python3 -m pip install flask-login

RUN pip3 freeze -> requirements.txt


COPY . /tourmeapp


CMD [ "python3", "app.py"]


