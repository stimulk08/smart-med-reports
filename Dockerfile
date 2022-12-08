FROM python:3.9.7-slim

EXPOSE 3000
WORKDIR /app

COPY ./app /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]