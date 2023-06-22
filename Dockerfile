FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

COPY ./app /app
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

ENV PATH="/py/bin:$PATH"