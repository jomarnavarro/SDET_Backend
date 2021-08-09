FROM python:3.8.11-alpine3.14

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD ["pytest"]