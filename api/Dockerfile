FROM python:3.9-alpine 

WORKDIR /app

COPY api.py .
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD uvicorn api:app --host 0.0.0.0 --reload

