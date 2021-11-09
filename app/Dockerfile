#docker file
# syntax=docker/dockerfile:1

FROM python:3.8



RUN python3 -m pip install flask-login

WORKDIR /tourmeapp

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip3 install --upgrade pip

RUN pip3 freeze -> requirements.txt


COPY . /tourmeapp


CMD [ "python3", "app.py"]


