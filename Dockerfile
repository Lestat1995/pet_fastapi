FROM python:3.11-slim

COPY . .

RUN pip install -r requiraments.txt

CMD ["uvicorn", "main.py", "--host", "0.0.0.0", "--port", "80"]
