FROM python:3.6


LABEL "com.github.actions.name"="Branch Cleanup"

LABEL "com.github.actions.description"="Send a text message to a specified phone if a PR is created"

LABEL "com.github.actions.icon"="activity"

LABEL "com.github.actions.color"="pink"


RUN mkdir /twilio
WORKDIR /twilio

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY text.py .

ENTRYPOINT ["python", "text.py"]
