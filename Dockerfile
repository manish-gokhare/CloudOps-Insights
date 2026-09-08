FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY data ./data
COPY static ./static
COPY templates ./templates
COPY run.py .

EXPOSE 5000

CMD ["python", "run.py"]