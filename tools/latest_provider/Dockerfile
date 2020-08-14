FROM python:3.8.5-alpine
EXPOSE 5000

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scripts/json_merger.py ./scripts/json_merger.py
COPY scripts/turtle.py ./scripts/turtle.py
COPY provider.py .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "provider:app"]
