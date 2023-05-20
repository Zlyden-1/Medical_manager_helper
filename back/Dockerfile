FROM python:3.10-alpine
LABEL authors="AntiVNSH-team"

RUN apt-get update && apt-get install -y gcc libpq-dev
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
COPY app /app
WORKDIR /app