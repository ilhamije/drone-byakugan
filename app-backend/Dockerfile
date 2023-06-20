# pull official base image
FROM python:3.8.0-alpine

# copy project
COPY . /app/

# set work directory
WORKDIR /app

# handle Pillow installation error
RUN apk add zlib-dev jpeg-dev gcc musl-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# run server
CMD python app.py
