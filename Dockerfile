FROM python:3.8.3-alpine

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 
COPY /src/. .
EXPOSE 80
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80"]
