FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /coffee-blog-api

RUN apt-get update \
  && apt-get -y install gcc \
  && apt-get clean

COPY ./requirements.txt /coffee-blog-api/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /coffee-blog-api/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]