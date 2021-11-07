# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=python_project/app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV LISTEN_PORT=80
RUN apk add --no-cache gcc musl-dev linux-headers
COPY python_project/requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80
COPY . .
CMD ["flask", "run"]