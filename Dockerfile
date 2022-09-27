ARG PYTHON_VERSION=3.9.4-alpine3.13

FROM python:${PYTHON_VERSION} as builder
ENV PYTHONUNBUFFERED=1

WORKDIR /wheels

RUN apk add --update --no-cache \
    alpine-sdk \
    postgresql-dev \
    gettext \
    jpeg-dev \
    zlib-dev 

COPY requirements.txt .
RUN pip wheel -r requirements.txt --disable-pip-version-check

FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED=1

RUN apk add --update --no-cache \
    libpq \
    postgresql-client

COPY --from=builder /wheels /wheels
RUN pip install \
        --no-cache-dir \
        --disable-pip-version-check \
        -r /wheels/requirements.txt \
        -f /wheels \
    && rm -rf /wheels

WORKDIR /app

COPY . ./
# RUN python manage.py collectstatic --no-input

ENV DJANGO_SETTINGS_MODULE='bbi_ecomm.settings_prod'
EXPOSE 8000

CMD ["uvicorn", "--host", "0.0.0.0", "bbi_ecomm.asgi:application"]