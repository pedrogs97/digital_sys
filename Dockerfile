FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

COPY ./app /app
COPY ./app/Pipfile /app/Pipfile
WORKDIR /app
EXPOSE 8000

RUN python -m pip install --upgrade pip && \
    # apt-get install build-dep python-psycopg2 && \
    pip install pipenv && pipenv install --dev --system --deploy && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol/web/media && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

USER django-user