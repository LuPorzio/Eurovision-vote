FROM python:3.9

WORKDIR /app

COPY data.py .
COPY utils/ utils/

RUN pip install redis bs4 requests

CMD [ "python", "data.py" ]