FROM python:3.8.5-alpine
EXPOSE 5000

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY scripts/*.py ./scripts/
COPY provider.py .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "provider:app"]
