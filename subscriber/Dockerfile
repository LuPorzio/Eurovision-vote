FROM python:3.9

WORKDIR /app

COPY subscriber.py .

RUN pip install redis fastapi uvicorn

CMD [ "uvicorn", "subscriber:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]