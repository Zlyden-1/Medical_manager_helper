FROM python:3.10-alpine
LABEL authors="AntiVNSH-team"

COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt
COPY app /app
WORKDIR /app