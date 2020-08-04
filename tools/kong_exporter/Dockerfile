FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY kong_api_exporter.py .

CMD ["gunicorn", "-b", "127.0.0.1:5000", "kong_api_exporter:app"]
