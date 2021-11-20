FROM ubuntu:20.04

RUN pip install -r requirements.txt
RUN python3 app.py