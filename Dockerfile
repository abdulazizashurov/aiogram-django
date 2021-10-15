FROM python:3.8.3-alpine

WORKDIR /home/app/web

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add postgresql-dev python3-dev gcc musl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

COPY ./entrypoint.sh .
COPY . .

ENTRYPOINT ["./entrypoint.sh"]