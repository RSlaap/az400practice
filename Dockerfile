FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY app.py app.py
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80"]