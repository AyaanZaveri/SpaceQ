FROM ubuntu:20.04

RUN sudo apt-get install python3-pip -y
RUN pip install -r requirements.txt
RUN python3 app.py