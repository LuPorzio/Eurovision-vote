FROM python:3.9

WORKDIR /app

COPY main.py .
COPY manager.py .
COPY page1.py .
COPY page2.py .
COPY requirements.txt .
COPY vote.py .
COPY utils/ utils/

RUN pip install -r requirements.txt

CMD [ "streamlit", "run", "manager.py" ]