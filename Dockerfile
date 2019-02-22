FROM python:3.6

RUN mkdir /twilio
WORKDIR /twilio

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY text.py .

ENTRYPOINT ["python", "text.py"]
