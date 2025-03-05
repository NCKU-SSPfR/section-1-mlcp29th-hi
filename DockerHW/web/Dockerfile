FROM python:3.11-slim

COPY requirements.txt .

RUN pip install --time 1000 --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["python", "main.py"]
