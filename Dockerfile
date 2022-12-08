FROM python:3.9.7-slim

EXPOSE 3000
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt