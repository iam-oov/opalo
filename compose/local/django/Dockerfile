FROM python:3-alpine

ENV PYTHONUNBUFFERED 1

# RUN apk update \
#   # psycopg2 dependencies
#   && apk add --virtual build-deps gcc python3-dev musl-dev \
#   && apk add postgresql-dev \
#   # Pillow dependencies
#   && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
#   # CFFI dependencies
#   && apk add libffi-dev py-cffi \
#   # Translations dependencies
#   && apk add gettext \
#   # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
#   && apk add postgresql-client

RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev g++ \
    libffi-dev openssl-dev \
    libxml2 libxml2-dev \
    libxslt libxslt-dev \
    libjpeg-turbo-dev zlib-dev \
    #   # psycopg2 dependencies
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r /requirements/local.txt

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
