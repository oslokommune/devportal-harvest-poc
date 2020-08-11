FROM python:3.8.5-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY kong.py .
COPY build ./build/

CMD ["python", "kong.py"]
