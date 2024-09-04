FROM ubuntu:latest
FROM python:latest
RUN apt-get update && apt-get upgrade -y \
    && apt-get install curl -y \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3 get-pip.py

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "db", "upgrade", "&&", "flask", "run", "--host=0.0.0.0"]

LABEL authors="max"
