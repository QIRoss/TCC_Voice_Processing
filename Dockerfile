FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install fastapi uvicorn

COPY . /app/

EXPOSE 5000

CMD ["uvicorn", "voice_api:app", "--host", "0.0.0.0", "--port", "5000"]
