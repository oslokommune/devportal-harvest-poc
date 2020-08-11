FROM python:3.8.5-alpine
EXPOSE 5000

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY provider.py .
COPY json_merger.py .

CMD ["gunicorn", "-b", "0.0.0.0:5000", "provider:app"]
