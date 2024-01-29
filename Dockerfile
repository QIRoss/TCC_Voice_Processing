FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

ENV FLASK_APP=voice_api.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install fastapi uvicorn

COPY . /app/

EXPOSE 5000

CMD ["flask", "run"]
