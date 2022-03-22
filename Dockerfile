# syntax=docker/dockerfile:1

FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install django
RUN export PATH="~/.local/bin/:$PATH"

COPY . /app/

EXPOSE 8000

CMD [ "python", "manage.py" , "runserver", "0.0.0.0:8000"]
