FROM python:3.12-slim-bullseye

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN mkdir -p app

COPY ./App /app

WORKDIR app

EXPOSE 5000

RUN ls -la /app 

CMD [ "python3", "app.py"]