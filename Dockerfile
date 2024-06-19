FROM python:3.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 10000
CMD flask run -h 0.0.0.0 -p 10000 & python3 main.py
