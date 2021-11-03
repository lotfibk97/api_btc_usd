FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /api
WORKDIR /api
ADD requirements.txt /api/
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ADD . /api/