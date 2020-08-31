FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY dataplatform-harvester.py .

CMD ["python", "dataplatform-harvester.py"]
