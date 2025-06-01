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

# 👇 Copy the original requirements.txt into /wheels so it can be installed
COPY requirements.txt /wheels/requirements.txt

RUN pip install \
    --no-cache-dir \
    --disable-pip-version-check \
    -r /wheels/requirements.txt \
    -f /wheels \
    && rm -rf /wheels

# Set working directory for your Django app
WORKDIR /app

# Copy all source code
COPY . .

# Optional: run collectstatic if you're serving static files with WhiteNoise
# RUN python manage.py collectstatic --no-input

# Make sure DJANGO_SETTINGS_MODULE points to the correct settings module
ENV DJANGO_SETTINGS_MODULE='bbi_ecomm.settings_prod'

EXPOSE 8000

# 🧠 Change this if you're using Django with WSGI instead of ASGI
CMD ["gunicorn", "bbi_ecomm.wsgi:application", "--bind", "0.0.0.0:8000"]
