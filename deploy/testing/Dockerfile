FROM python:3.10-slim-buster
LABEL maintainer="sa5mchavez"
WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements-dev.txt
RUN pip install --no-cache-dir -r requirements.txt


