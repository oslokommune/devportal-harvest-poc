FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY json_merger.py .
COPY dataplatform.py .

CMD ["python", "dataplatform.py"]
