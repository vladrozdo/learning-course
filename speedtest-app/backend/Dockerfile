FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install fastapi uvicorn mysql-connector-python speedtest-cli

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
