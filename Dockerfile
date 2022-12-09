FROM python:3.9.7-slim

EXPOSE 8000
WORKDIR /code

COPY ./app /code/app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
